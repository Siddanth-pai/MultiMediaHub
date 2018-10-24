from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image
#class Users(models.Model):
#    username = models.CharField(primary_key=True, max_length=100)
#    password = models.CharField(max_length=100)
#    email = models.CharField(max_length=100)
#    album_logo = models.CharField(max_length=1000)

#class Admins(models.Model):
#    username = models.CharField(primary_key=True, max_length=100)
#    password = models.CharField(max_length=100)
#    email = models.CharField(max_length=100)

#class Videos(models.Model):
#    videoid = models.IntegerField(primary_key=True, max_length=1000)
#    videotitle = models.CharField(max_length=100)
#    videologo = models.CharField(max_length=100)
#    releasedate = models.DateField()

class Songs(models.Model):
    songid = models.AutoField(primary_key=True,null=False)
    artist = models.CharField(max_length=100)
    songtitle = models.CharField(max_length=100)
    albumtitle = models.CharField(max_length=100)
    albumlogo =  models.ImageField(default = 'default.jpg',upload_to='_logo_pics')
    releasedate = models.DateField()
    genre = models.CharField(max_length=100)
    audiofile= models.FileField(upload_to='audios/',null = True,verbose_name="")

    def __str__(self):
        return self.songtitle + ' by ' + self.artist
#class VideoDetails(models.Model):
#    videoid = models.ForeignKey(Videos, max_length=1000)

#class SongsDetails(models.Model):a
#    songid = models.ForeignKey(Songs, max_length=1000)

class SongDetails(models.Model):
    songid = models.ForeignKey('Songs',on_delete=models.CASCADE)
    songhits = models.IntegerField()
    username = models.ForeignKey(User,on_delete= models.CASCADE)
    #is_favourite = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    #image = models.ImageField(default = 'default.jpg',upload_to='_profile_pics')
    image = models.ImageField(default = 'default.jpg',upload_to='_profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'




class Videos(models.Model):
    videoid = models.AutoField(primary_key=True,null=False)
    #artist = models.CharField(max_length=100)
    videotitle = models.CharField(max_length=100)
    #albumtitle = models.CharField(max_length=100)
    #albumlogo =  models.ImageField(default = 'default.jpg',upload_to='_logo_pics')
    releasedate = models.DateField()
    #genre = models.CharField(max_length=100)
    videofile= models.FileField(upload_to='videos/',null = True,verbose_name="")


class VideoDetails(models.Model):
    videoid = models.ForeignKey('Videos',on_delete=models.CASCADE)
    videohits = models.IntegerField()
    username = models.ForeignKey(User,on_delete= models.CASCADE)
