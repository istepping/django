from urllib import request
from urllib import parse
import json
import time


def get_lng_and_lat(city):
    city = parse.quote(city)
    url = "http://api.map.baidu.com/geocoder?key=37492c0ee6f924cb5e934fa08c6b1676&&output=json&address=" + city
    with request.urlopen(url) as f:
        res = f.read()
        data = json.loads(res.decode('utf-8'))
        print(data)
    return [data["result"]["location"]["lng"], data["result"]["location"]["lat"]]


def get_visual_data_with_end(start_city, end_city):
    data = list()
    print(end_city)
    item = {
        "from": {"name": start_city, "coordinates": get_lng_and_lat(start_city)},
        "to": {"name": end_city, "coordinates": get_lng_and_lat(end_city)},
        "count": 1
    }
    data.append(item)
    return data


def get_visual_data(start_city):
    date = "2018-12-21"
    data = list()
    end_city = ["上海", "北京", "合肥", "福建", "兰州", "贵阳", "石家庄", "武汉", "长沙", "长春", "吉林", "南京", "南昌", "沈阳", "济南",
                "太原", "郑州", "四川", "杭州", "昆明"]
    lng_and_lat = get_lng_and_lat(start_city)
    for end in end_city:
        # response = json.loads(get_airplane_data(start_city, end, date))
        print(end)
        if end != start_city:
            item = {
                "from": {"name": start_city, "coordinates": lng_and_lat},
                "to": {"name": end, "coordinates": get_lng_and_lat(end)},
                "count": 1
            }
            data.append(item)
    print(data)
    return data


def get_airplane_data(start_city, end_city, date):
    # 数据请求
    print(start_city)
    print(end_city)
    start_city = parse.quote(start_city)
    end_city = parse.quote(end_city)
    url = "http://apicloud.mob.com/flight/line/query?key=520520test&start=" + start_city + "&end=" + end_city
    with request.urlopen(url) as f:
        res = f.read()
        return res.decode('utf-8')


def get_weather_data(city):
    # 数据请求
    city = parse.quote(city)
    url = "https://www.tianqiapi.com/api/?version=v1&city=" + city
    with request.urlopen(url) as f:
        res = f.read()
        print(res.decode('utf-8'))
        return res.decode('utf-8')
