#  -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
import algo.bill as billing
import numpy as np


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
        class_ratio = billing.predict(np.array(
            [round(float(param1), 2), round(float(param2), 2), round(float(param3), 2), round(float(param4), 2),
             round(float(param5), 2), round(float(param6), 2)]))
        context['message'] = 'success'
        context['status'] = '1'
        context['aReason'] = str(class_ratio[0] * 100) + "%"
        context['aImpluse'] = str(class_ratio[1] * 100) + "%"
        context['aRandom'] = str(class_ratio[2] * 100) + "%"
        context['aHabit'] = str(class_ratio[3] * 100) + "%"
        context['aCollection'] = str(class_ratio[4] * 100) + "%"
        context['aImagine'] = str(class_ratio[5] * 100) + "%"
        return HttpResponse(json.dumps(context), content_type='application/json')
    else:
        context['message'] = 'param error!'
        context['status'] = '0'
        return HttpResponse(json.dumps(context), content_type='application/json')
