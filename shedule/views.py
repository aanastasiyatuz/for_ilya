from django.shortcuts import render

from .serializers import *

def generate_html():
    from algorithm.ConsoleApp import main
    main("/algorithm/inai.json")

def generate_shedule(request):
    if request.GET.get("q") == 'create':
        get_json()
        generate_html()
    return render(request, "shedule.html")


