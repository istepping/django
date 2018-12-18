#  -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test


def hello(request):
    context = dict()
    context['hello'] = 'hello world*'
    return render(request, 'hello.html', context)


def insert_data(request):
    test1 = Test(name='sunLei')
    test1.save()
    return HttpResponse('成功插入一条数据')
