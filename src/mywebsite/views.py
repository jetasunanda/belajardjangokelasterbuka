from django.http import HttpResponse
from django.shortcuts import render

# method view index
def index(request):
    context = {
        'judul':'Warteg',
        'subjudul':'Selamat datang',
        'kontributor':'bambang',
        'nav': [
            ['/' , 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact'],
        ]
    }
    return render(request, 'index.html', context)