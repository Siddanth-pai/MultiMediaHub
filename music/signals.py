from django.db.models.signals  import post_save# signal that is created when a post is saved
from django.contrib.auth.models import User# acts like a sender
from django.dispatch import receiver
from .models import Profile
#this file is used to add a profile photo to every new user that is created
# **kwargs takes in any additinal arguements
@receiver(post_save,sender=User)#when  a user is saved then send this signal to receiver....then this receiver is this fun ...it takes all the arguements that post_save signals has sent and
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)#when  a user is saved then send this signal to receiver....then this receiver is this fun ...it takes all the arguements that post_save signals has sent and
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
