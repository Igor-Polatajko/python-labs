#!/usr/bin/env python
import csv

import requests
from bs4 import BeautifulSoup

PAGE_LINK = "http://www.codeabbey.com/index/user_ranking"


def scrap_info():
    content = requests.get(PAGE_LINK, headers={"User-Agent": "XY"}).content
    soup = BeautifulSoup(content, 'lxml')
    ranking_table = soup.find("table", {"class": "ranking-table"})
    rows = ranking_table.find_all("tr")

    data = []
    for row in rows[1::]:
        cols = list(map(lambda r: r.text.strip(), row.find_all("td")))
        data.append({'rate_position': cols[0],
                     'username': cols[2],
                     'rank': cols[4],
                     'enlightenment': cols[5],
                     'solved': cols[6]})
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
    data = scrap_info()
    write_to_csv("data.csv", data)


if __name__ == '__main__':
    main()
