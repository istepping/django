from urllib import request
from urllib import parse


def get_airplane_data(start_city, end_city, date):
    # 数据请求
    start_city = parse.quote(start_city)
    end_city = parse.quote(end_city)
    url = "https://flight.qunar.com/touch/api/domestic/wbdflightlist?departureCity=" + start_city + "&arrivalCity=" + end_city + "&departureDate=" + date
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

    with request.urlopen(req) as f:
        res = f.read()
        print(res.decode('utf=8'))
        return res.decode('utf-8')
    # 数据处理
    # 数据返回
