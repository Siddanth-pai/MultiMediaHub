#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    # /music/
    path('', views.index, name = 'index'),
    path('audi/',views.showaudio,name = 'showaudio'),
    path('video/',views.showvideo,name = 'showvideo'),

    #/music/17/ ---> music/'songid'
    path('post/<videoid>', views.videodetail, name='videodetail'),
    path('comment/<songid>', views.add_comment_to_post, name='add_comment_to_post'),
    #path('vcomment/<videoid>', views.add_comment_to_post_video, name='add_comment_to_post_video'),

    path('<songid>', views.detail, name='detail'),
]


# ('<int:album_id>', views.detail)
