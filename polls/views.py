from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Hello, you are at index')


def something(request):
    return render()