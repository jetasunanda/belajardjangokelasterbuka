#views blog
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul':'blog',
        'kontributor':'anto',
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul':'news',
        'kontributor':'otong',
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul':'cerita',
        'kontributor':'budi',
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse('<h1>Ini adalah recent post</h1>')