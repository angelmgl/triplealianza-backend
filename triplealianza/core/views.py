from django.shortcuts import render
from django.http import JsonResponse

def welcome(request):
    response = {'title': 'Welcome to triplealianza.com.py!'}
    return JsonResponse(response)