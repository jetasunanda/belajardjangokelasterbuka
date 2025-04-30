from django.http import HttpResponse
from django.shortcuts import render

# method view index
def index(request):
    context = {
        'judul':'Warteg',
        'kontributor':'bambang',
    }
    return render(request, 'index.html', context)