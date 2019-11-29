#!/usr/bin/env python
import csv
import random
import re
from time import sleep

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://price.ua/catc839t14/page"


def parse_price(price):
    price = price.replace(' &nbspгрн.', '')
    return list(map(lambda p: re.sub(r'\D', '', p), price.split('—')))


def fetch_processor_info(description):
    def _find_by_keyword(keyword):
        rows = description.find_all('tr')
        for r in rows:
            name = r.find('td', {'class': 'td-name'}).find('div', 'relative-wrap').text
            value = r.find('td', {'class': 'td-value'}).find('div', 'relative-wrap').text
            if keyword in name:
                return value

    processor = _find_by_keyword('Процессор')
    if processor is not None:
        return processor

    processor_type = _find_by_keyword('Тип процессора')
    if processor_type is not None:
        return processor_type

    return 'Not specified'


def scrap_data(pages_limit=None):
    previous_content = None
    page_counter = 1
    data = []
    while True:
        content = requests.get(f"{BASE_URL}{page_counter}.html", headers={"User-Agent": "XY"}).content

        if (pages_limit and pages_limit < page_counter) or previous_content == content:
            return data

        soup = BeautifulSoup(content, 'lxml')
        product_blocks = soup.find_all('div', {'class': 'product-block'})

        for product in product_blocks:
            link = product.find('a', {'class': 'model-name ga_card_mdl_title'})
            name = re.sub(r'^[^\s]+\s', '', link.text)
            link_url = link['href'].strip()
            photo_url = soup.find('span', {'class': 'ga_card_mdl_pic'}).find('img')['src'].strip()[2::]
            print(f"Visit url {link_url}")
            product_page = requests.get(link_url, headers={"User-Agent": "XY"}).content
            product_page_soup = BeautifulSoup(product_page, 'lxml')
            price = parse_price(product_page_soup.find('div', {'class': 'price-diapazon'}).text)

            processor = fetch_processor_info(
                product_page_soup.find('table', {'class': 'description producer-under-descr'}))

            if 10000 < int(price[0]) and int(price[1]) < 20000:
                data.append({'name': name,
                             'min_price': price[0],
                             'max_price': price[1],
                             'processor': processor,
                             'link': link_url,
                             'photo_link': photo_url})
            sleep(random.uniform(0.01, 0.3))

        page_counter += 1
        sleep(random.random())


def write_to_csv(file_path, data):
    with open(file_path, mode='w', newline='') as csv_file:
        if len(data) < 1:
            return
        writer = csv.DictWriter(csv_file, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    data = scrap_data(1)
    write_to_csv('lab_16_2.csv', data)


if __name__ == '__main__':
    main()
