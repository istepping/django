#  -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from . import data


def get_visual_data(request):
    return 0


def get_weather_data(request):
    context = dict()
    request.encoding = 'utf-8'
    if 'city' in request.GET:
        city = request.GET['city']
        res = data.get_weather_data(city)
        return HttpResponse(res, content_type='application/json')
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
        return HttpResponse(json.dumps(context), content_type='application/json')


def get_airplane_data(request):
    context = dict()
    request.encoding = 'utf-8'
    if 'startCity' in request.GET and 'endCity' in request.GET:
        start_city = request.GET['startCity']
        end_city = request.GET['endCity']
        date = request.GET['date']
        res = data.get_airplane_data(start_city, end_city, date)
        return HttpResponse(res, content_type='application/json')
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
        return HttpResponse(json.dumps(context), content_type='application/json')
