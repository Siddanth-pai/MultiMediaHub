from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Songs,Videos,SongDetails,VideoDetails


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()



    class Meta: # this class gives us nested namespace for configuarations and keeps the configuartions at one place....forms.save will save in thb euser model
         model = User
         fields = ('username','email','password1',)




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image']


class AudioForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields=["songid","artist","songtitle","albumtitle","albumlogo","releasedate","genre","audiofile"]



class SongCommentForm(forms.ModelForm):
    class Meta:
        model = SongDetails
        fields = ("text","username")


class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = VideoDetails
        fields = ("text","username")



class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields=["videoid","videotitle","releasedate","videofile"]
