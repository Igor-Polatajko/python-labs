#!/usr/bin/env python
import csv

import requests
from bs4 import BeautifulSoup

FIELDS_TO_SCRAP = ['Повна назва', 'Скорочена', 'Телефони', 'E-mail', 'Директор',
                   'Кількість учнів', 'Кількість класів', 'Кількість приміщень']


def scrap_info_from_page(page_link, fields_to_scrap):
    pass


def fetch_page_link_from_row(row):
    cols = row.find_all('td')
    if len(cols) < 2:
        return ''
    return cols[1].find('a')['href']


def decode_email(email):
    return email


def scrap_info_from_list_page(list_page_link):
    page_content = requests.get(list_page_link, headers={"User-Agent": "XY"}).content
    page_soup = BeautifulSoup(page_content, 'lxml')
    rows = page_soup.find('table', {'class': 'zebra-stripe list'}).find_all('tr')[1::]
    page_links = list(filter(lambda link: link, [fetch_page_link_from_row(row) for row in rows]))
    data = [scrap_info_from_page(page_link, FIELDS_TO_SCRAP) for page_link in page_links]
    for d in data:
        d['email'] = decode_email(d['email'])
    return data


def write_to_csv(file_path, data):
    with open(file_path, mode='w', newline='') as csv_file:
        if len(data) < 1:
            return
        writer = csv.DictWriter(csv_file, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    data = scrap_info_from_list_page('https://if.isuo.org/authorities/schools-list/id/626')
    # write_to_csv('lab_16_2.csv', data)


if __name__ == '__main__':
    main()
