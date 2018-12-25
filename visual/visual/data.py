from urllib import request
from urllib import parse
import json


def get_visual_data(start_city, end_city, date):
    response = json.load(get_airplane_data(start_city, end_city, date))
    print(response)
    item = {
        "from": {"name": response.result[0].fromCityName, "coordinates": [113.270793, 23.135308]},
        "to": {"name": response.result[0].toCityName, "coordinates": [112.612787, 27.317599]},
        "count": 1
    }
    data = list()
    data.append(item)
    print(data)
    return data


def get_airplane_data(start_city, end_city, date):
    # 数据请求
    start_city = parse.quote(start_city)
    end_city = parse.quote(end_city)
    url = "http://apicloud.mob.com/flight/line/query?key=520520test&start=" + start_city + "&end=" + end_city
    with request.urlopen(url) as f:
        res = f.read()
        print(res.decode('utf-8'))
        return res.decode('utf-8')


def get_weather_data(city):
    # 数据请求
    city = parse.quote(city)
    url = "https://www.tianqiapi.com/api/?version=v1&city=" + city
    with request.urlopen(url) as f:
        res = f.read()
        print(res.decode('utf-8'))
        return res.decode('utf-8')
