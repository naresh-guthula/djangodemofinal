from django.shortcuts import render
from django.http import HttpResponse
from os import environ
from time import ctime


# Create your views here.

def index(request):
    return HttpResponse('Hello & Hi............')


def printenv(request):
    context = dict(env=environ, ts=ctime())
    return render(request, 'env.html', context)
