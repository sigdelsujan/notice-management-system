from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122, null= True, blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Notice(models.Model):
    title = models.CharField(max_length=122)
    desc = models.TextField(null= True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title
