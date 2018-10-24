from django.contrib import admin
from .models import Songs,SongDetails,Profile,Videos,VideoDetails
# Register your models here.

admin.site.register(Songs)
admin.site.register(SongDetails)
admin.site.register(Profile)
admin.site.register(Videos)
admin.site.register(VideoDetails)
