from django.shortcuts import render
from django.http import JsonResponse

def welcome(request):
    response = {'title': 'Welcome!'}
    return JsonResponse(response)