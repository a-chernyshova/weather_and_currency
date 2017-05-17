# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import lxml

URL = 'http://ligovka.ru/detailed/amerikanskij-dollar'


def get_html(url):
    response = request.urlopen(url)
    return response.read()


def parse(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('table', class_='frame prices')
    rows = content.find_all('tr')[1:11]
    tendency = []
    for row in rows:
        col = row.find_all('td')[2:3]
        tendency.append(col[0].text)
    return tendency


def print_tendency(tendency):
    for i in tendency:
        print(i)


def analytics(url):
    tendency = parse(url)
    print('$ vs ruble (10 days)')
    print(' Today: ', tendency[0])
    print(' Min:   ', min(tendency))
    print(' Max:   ', max(tendency), '\n')
    return tendency


def print_tendency(tendency):
    # TODO: cost changes diagram
    pass


def advice(url):
    tendency = parse(url)
    current = tendency[0]
    tendency.sort()
    current_index = tendency.index(current)
    if current_index <= 1:
        print('Advice: The best price during last 10 days\n')
    elif current_index < 5:
        print("Advice: The price is better then other 50%\n You need to double check tendency before buy or sell\n")
    else:
        print("Advice: It is better to wait\n")


def main():
    analytics(URL)
    advice(URL)
    #print_tendency(analytics(URL))

if __name__ == '__main__':
    main()

# TODO: custom amount of day to analyse