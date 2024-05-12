from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>PROYECTO EN CONSTRUCCIÓN</h1><h2>Jeniffer Dueñas:)</h2>")