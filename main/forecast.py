# -*- coding: utf-8 -*-
from urllib import request
import json
import datetime


TIMESTAMP = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
API1 = 'https://www.theweathernetwork.com/us/api/data/usny0996/ci?ts=1752'


def get_html(url):
    response = request.urlopen(url)
    return response.read()


def parse(url):
    json_ = get_html(url)
    result = json.loads(json_)['obs']
    global params
    params = {}

    params['sky'] = result['wxc'] + ' ' + result['wxca']
    params['sunset'] = result['sunrise_time']
    params['sunrise'] = result['sunset_time']
    params['uv'] = result['uv_level_icon']
    params['wind direction'] = result['windDirection_icon']
    params['wind'] = int(result['w'] * 1.6 * 1000 / 3600)  # mph to mps
    params['humidity'] = result['h']
    params['temperature'] = result['t']
    params['feels like'] = result['f']
    params['pressure'] = result['pressure_icon']
    params['changes'] = result['wxsp']

    return params


def advice(params):
    print('Some pieces of advice:')
    temper = int(params['feels like'])
    if temper > 15 and temper < 22:
        print('It is quite warm.')
    elif temper > 22:
        print("It's better to summer wear and take water with you.")
    if int(params['humidity']) > 80:
        print('It may be rainy. Take umbrella.')
    if params['sky'] == 'Clear sunny':
        print('Take sunglasses')
    if params['uv'] == 'high':
        print('Use sun protector cream')
    if params['pressure'] == 'medium-high' or params['pressure'] == 'high':
        print('Be careful, it is high pressure, you may feel headache')
    if params['changes'] == 'PRECIP':
        print('Take umbrella. It is going to be rainy')


def print_weather_forecast(url):
    params = parse(url)
    report = '{:<17}{}C\n{:<17}{}C\n{:<17}{}\n{:<17}{}\n{:<17}{}\n{:<17}{} ' \
             'm/s\n{:<17}{}%\n{:<17}{}\n{:<17}{}\n{:<17}{}\n{:<17}{}' \
             '\n'.format('Temperature:', params['temperature'], 'Feels like:', params['feels like'],
                         'Sky is:', params['sky'], 'UV level:', params['uv'], 'Wind direction:',
                         params['wind direction'], 'Wind:', params['wind'], 'Humidity:', params['humidity'],
                         'Pressure:', params['pressure'], 'Next 3 hours: ', params['changes'],
                         'Sunrise:', params['sunrise'], 'Sunset:', params['sunset'])
    print(report)


def write_statistic():
    with open('weather_stats.txt', 'a+', encoding='utf-8') as f:
        f.write(TIMESTAMP + str(params)+'\n')
        f.close()


def main():
    print_weather_forecast(API1)
    advice(parse(API1))
    write_statistic()


if __name__ == '__main__':
    main()


# TODO: change location - list of 3 send request with argument
# TODO: запуск каждый день по веремени автоматически для сбора статистики
