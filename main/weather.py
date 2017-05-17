# -*- coding: utf-8 -*-
from urllib import request
import json


API = 'https://www.theweathernetwork.com/us/api/savedlocation/index/?placecodes=USNY0996'


def get_html(url):
    response = request.urlopen(url)
    return response.read()


def parse(link):
    json_ = get_html(link)
    result = json.loads(json_)
    result = result[0]
    today = result['updatetime']
    temperature = result["temperature"]
    t_feels_like = result["feels_like"]
    sky = result['wxcondition']
    report = 'Today: {}\nTemperature: {}C\nFeels like: {}C\nSky is: {}\n'.format(today, temperature, t_feels_like, sky)
    print(report)
    return report


def main():
    parse(API)


if __name__ == '__main__':
    main()
