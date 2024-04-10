from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def lesson(request):
    return HttpResponse('<h1>Это страница, которую от меня хочут((</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Нет такой страницы</h1>')
