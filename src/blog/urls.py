from django.urls import path

from . import views

urlpatterns = [
    path('recent/', views.recent),
    path('cerita/', views.cerita),
    path('news/', views.news),
    path('', views.index),
]
