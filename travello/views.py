from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def api(request):
    return HttpResponse("API HERE")

def add(request):
    try:
        num1 = request.GET["num1"]
        num2 = request.GET["num2"]
        add = int(num1) + int(num2)
        result = json.dumps({"result": add})
        return HttpResponse(result)
    except KeyError:
        return HttpResponse("Query missing")