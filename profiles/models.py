from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=20, default='', blank=True)

    def __str__(self):
        return self.nickname

    def __unicode__(self):
        return self.nickname


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)


'''
set profile method
In [1]: from django.contrib.auth.models import User

In [2]: user = User.objects.get(pk=2)

In [3]: user.userprofile
Out[3]: <UserProfile: >

In [4]: p = user.userprofile

In [5]: p.nickname = "ss"

In [6]: p.save()




'''