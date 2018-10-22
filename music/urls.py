#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    #/music/17/ ---> music/'songid'
    path('<songid>', views.detail, name='detail'),
]


# ('<int:album_id>', views.detail)
