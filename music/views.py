from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
#from django.template import loader
#from django.shortcuts import render
from .models import Songs,Profile
from django.contrib import messages
# Create your views here
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,AudioForm
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def register(request):
   #form = UserCreationForm()
  # return render(request,'music/register.html',{'form':form})






    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :# checks for passwords and if user already existed,
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')#flash messages are temporary they appear only once on reload they disappear
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'music/register.html',{'form': form})


def index(request):
    #return HttpResponse("<h2><i>This is the Music app homepage</i></h2>")
    all_songs = Songs.objects.all()
    return render(request, 'music/index.html', {'all_songs': all_songs})
    #template = loader.get_template('music/index.html')
    ######
    #DICTIONARY TO STORE INFO THAT TEMPLATE NEEDS
    ######

    #context = {
    #'all_songs': all_songs,
#}

    #html = ''
    #for song in all_songs:
    #    url = '/music/' + str(song.songid)
    #    html += '<a href="' + url +'">' + song.songtitle + '</a><br>'
    #return HttpResponse(template.render(context, request))
    #return render(request, 'music/index.html', {'all_songs': all_songs})

def detail(request, songid):
#    try:
#        song = Songs.objects.get(pk=songid)
#    except Songs.DoesNotExist:
#        raise Http404("Song does not exist")
    #return HttpResponse("<h2> Details for Song ID :" + str(songid) + "</h2>")
    song = get_object_or_404(Songs, pk=songid)
    return render(request, 'music/detail.html', {'song': song} )

@login_required# decorators add functionality to an existing function
def profile(request):


    all_users = Profile.objects.all()



#    if request.method == 'POST':
#        u_form = UserUpdateForm(request.POST, instance=request.user)
#        p_form = ProfileUpdateForm(request.POST,
#                                   request.FILES,
#                                   instance=request.user.profile)
#        if u_form.is_valid() and p_form.is_valid():
#            u_form.save()
#            p_form.save()
#            messages.success(request, f'Your account has been updated!')
#            return redirect('profile')

#    else:
#        u_form = UserUpdateForm(instance=request.user)
#        p_form = ProfileUpdateForm(instance=request.user.profile)

#    context = {
#        'u_form': u_form,
#        'p_form': p_form
#    }


    return render(request, 'music/profile.html', {'all_users':all_users})


#def favourite(request, songid):
#    song = get_object_or_404(Songs, pk=songid)
#    try:
#        selected_song = Songs.objects.get(pk=request.POST['song'])
#    except (KeyError, Song.DoesNotExist):
#        return render(request, 'music/detail.html', {'song': song,
#        error_message: "Not a valid song yo!",} )
#    else:
#        selected_song.is_favourite = True
#        selected_song.save()
#        return render(request, 'music/detail.html', {'song': song} )




def showaudio(request):
    # lastaudio = Songs.objects.all()
  if request.method == 'POST':
        form = AudioForm(request.POST or None,request.FILES or None)
        if form.is_valid():
           form.save()
           audios = form.cleaned_data.get('songtitle')
           messages.success(request,f' created for {audios}!')
           return redirect('music:index')
  else:
       form =  AudioForm()

     #context = {'lastaudio':lastaudio,'form':form}
  return render(request,'music/audi.html',{'form':form})
