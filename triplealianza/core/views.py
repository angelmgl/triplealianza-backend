from django.shortcuts import render
from django.http import JsonResponse

def welcome(request):
    response = {
        'title': 'Welcome to triplealianza.com.py!',
        'description': 'Hey! We are under construction right now, but don\'t worry! We are working hard to get everything ready soon and provide you with the best content! Thanks for your patience and see you soon! 🚧👷‍♂️👷‍♀️'
    }
    return JsonResponse(response)