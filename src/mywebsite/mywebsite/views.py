from django.http import HttpResponse
from django.shortcuts import render

# method view index
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')