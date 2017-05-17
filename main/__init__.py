# -*- coding: utf-8 -*-
from main import currensy
from main import tendency
from main import weather
from main import forecast


API = 'https://www.theweathernetwork.com/us/api/savedlocation/index/?placecodes=USNY0996'
API1 = 'https://www.theweathernetwork.com/us/api/data/usny0996/ci?ts=1752'
URL = 'http://ligovka.ru/'
URL1 = 'http://ligovka.ru/detailed/amerikanskij-dollar'

currensy.print_currency(URL)
#tendency.analytics(URL1)
#tendency.advice(URL1)

#forecast.print_weather_forecast(API1)
forecast.advice(forecast.parse(API1))
