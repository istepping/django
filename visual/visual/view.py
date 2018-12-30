#  -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from . import data


def get_visual_data_with_end(request):
    context = dict()
    request.encoding = 'utf-8'
    response = HttpResponse(content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    if 'startCity' in request.GET and "endCity" in request.GET:
        start_city = request.GET['startCity']
        end_city = request.GET["endCity"]
        print(end_city)
        res = data.get_visual_data_with_end(start_city, end_city)
        response.write(json.dumps(res))
        return response
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
        response.write(json.dumps(context))
        return response


def get_visual_data(request):
    context = dict()
    request.encoding = 'utf-8'
    response = HttpResponse(content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    if 'startCity' in request.GET:
        start_city = request.GET['startCity']
        res = data.get_visual_data(start_city)
        response.write(json.dumps(res))
        return response
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
        response.write(json.dumps(context))
        return response


def get_weather_data(request):
    context = dict()
    request.encoding = 'utf-8'
    response = HttpResponse(content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    if 'city' in request.GET:
        city = request.GET['city']
        res = data.get_weather_data(city)
        response.write(res)
        return response
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
        response.write(json.dumps(context))
        return response


def get_airplane_data(request):
    context = dict()
    request.encoding = 'utf-8'
    if 'startCity' in request.GET and 'endCity' in request.GET:
        start_city = request.GET['startCity']
        end_city = request.GET['endCity']
        date = "2018-12-21"
        res = data.get_airplane_data(start_city, end_city, date)
        response = HttpResponse(res, content_type='application/json')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
        response = HttpResponse(json.dumps(context), content_type='application/json')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
