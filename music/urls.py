#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    # /music/
    path('', views.index, name = 'index'),
    path('audi/',views.showaudio,name = 'showaudio'),
    #/music/17/ ---> music/'songid'
    path('<videoid>', views.videodetail, name='detail'),
    path('<songid>', views.detail, name='detail'),
]


# ('<int:album_id>', views.detail)
