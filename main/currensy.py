# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup


URL = 'http://ligovka.ru/'


def get_html(url):
    response = request.urlopen(url)
    return response.read()


def parse(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('table', class_='table_course')
    rows = content.find_all('tr')[2:3]  # выбрана одна строка - можно выбрать несколько
    currency = {}
    for row in rows:
        col = row.find_all('td')[2:]
        currency['$ buy'] = col[0].a.text
        currency['$ sell'] = col[1].a.text
        currency['euro buy'] = col[3].a.text
        currency['euro sell'] = col[4].a.text

    file = open('currency_stats.txt', 'a+')
    file.write(str(currency)+'\n')
    file.close()
    return currency


def print_currency(url):
    currency = parse(url)
    print('{0:_^20}'.format('Currency today'))
    for key, value in currency.items():
        print('{:<14} {:<5}'.format(key, value))
    print('_'*20)


def main():
    print_currency(URL)

if __name__ == '__main__':
    main()
