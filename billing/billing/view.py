#  -*- coding: utf-8 -*-
from django.http import HttpResponse
import json


def get_action(request):
    context = dict()
    request.encoding = 'utf-8'
    if 'param1' in request.GET and 'param2' in request.GET and 'param3' in request.GET and 'param4' in request.GET and 'param5' in request.GET and 'param6' in request.GET:
        param1 = request.GET['param1']
        param2 = request.GET['param2']
        param3 = request.GET['param3']
        param4 = request.GET['param4']
        param5 = request.GET['param5']
        param6 = request.GET['param6']
        # 调用算法
        context['message'] = 'success'
        context['status'] = '1'
        context['1'] = '0.7'
        context['2'] = '0.8'
        context['3'] = '0.9'
        context['4'] = '0.5'
        context['5'] = '0.5'
        context['6'] = '0.6'
        return HttpResponse(json.dumps(context), content_type='application/json')
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
        return HttpResponse(json.dumps(context), content_type='application/json')
