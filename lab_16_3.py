#!/usr/bin/env python
import codecs
import csv
import random
from time import sleep
from urllib.parse import urlsplit

import js2py as js2py
import requests
from bs4 import BeautifulSoup

FIELDS_TO_SCRAP = ['Повна назва', 'Скорочена', 'Телефони', 'E-mail', 'Директор',
                   'Кількість учнів', 'Кількість класів', 'Кількість приміщень']


def ensure_data_integrity(data, fields_required):
    for field in fields_required:
        if field not in data.keys() or not data[field]:
            data[field] = 'not specified'


def decode_email(email):
    js_code = email[15:-24]
    email_link = js2py.eval_js(js_code)
    email_soup = BeautifulSoup(email_link, 'lxml')
    return email_soup.text


def remove_newlines(line):
    return ' '.join(line.rsplit())


def scrap_info_from_page(page_link, fields_to_scrap):
    print(f"Visit url {page_link}")
    sleep(random.uniform(0.01, 0.3))
    page_content = requests.get(page_link, headers={"User-Agent": "XY"}).content
    page_soup = BeautifulSoup(page_content, 'lxml')
    data_table = page_soup.find('table', {'class': 'zebra-stripe'})
    rows = data_table.find_all('tr')
    result = {}
    for row in rows:
        name = row.find('th')
        value = row.find('td')

        if not name or not value:
            continue

        name = name.text
        fields_match = [field for field in fields_to_scrap if field in name]
        if len(fields_match) > 0:
            field = fields_match[0]
            if 'E-mail' in name:
                href = value.find('a')
                if href:
                    result[field] = remove_newlines(decode_email(href['onclick']))
                continue
            result[field] = remove_newlines(value.text)
            ensure_data_integrity(result, fields_to_scrap)
    return result


def fetch_page_link_from_row(row):
    cols = row.find_all('td')
    if len(cols) < 2:
        return ''
    return cols[1].find('a')['href']


def get_domain(url):
    return "{0.scheme}://{0.netloc}".format(urlsplit(url))


def scrap_info_from_list_page(list_page_link):
    page_content = requests.get(list_page_link, headers={"User-Agent": "XY"}).content
    page_soup = BeautifulSoup(page_content, 'lxml')
    rows = page_soup.find('table', {'class': 'zebra-stripe list'}).find_all('tr')[1::]
    page_links = list(filter(lambda link: link, [fetch_page_link_from_row(row) for row in rows]))
    domain = get_domain(list_page_link)
    page_links = list(map(lambda link: domain + link, page_links))
    return [scrap_info_from_page(page_link, FIELDS_TO_SCRAP) for page_link in page_links]


def write_to_csv(file_path, data):
    with codecs.open(file_path, 'w', 'utf-8') as csv_file:
        if len(data) < 1:
            return
        writer = csv.DictWriter(csv_file, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    data = scrap_info_from_list_page('https://if.isuo.org/authorities/schools-list/id/626')
    write_to_csv('lab_16_3.csv', data)


if __name__ == '__main__':
    main()
