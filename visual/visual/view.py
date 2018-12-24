#  -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from . import data


def get_airplane_data(request):
    context = dict()
    request.encoding = 'utf-8'
    if 'startCity' in request.GET and 'endCity' in request.GET and 'date' in request.GET:
        start_city = request.GET['startCity']
        end_city = request.GET['endCity']
        date = request.GET['date']
        context['message'] = 'success'
        context['status'] = '1'
        context['data'] = data.get_airplane_data(start_city, end_city, date)
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
    return HttpResponse(json.dumps(context), content_type='application/json')
