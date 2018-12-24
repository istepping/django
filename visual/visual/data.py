from urllib import request
from urllib import parse


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
