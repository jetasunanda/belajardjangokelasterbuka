#views blog
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul':'Warteg',
        'subjudul':'Blog',
        'kontributor':'anto',
        'nav': [
            ['/', 'Home'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News'],
        ]
    }
    return render(request, 'index.html', context)

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