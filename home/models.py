# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Application(models.Model):

    #__Application_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Application_FIELDS__END

    class Meta:
        verbose_name        = _("Application")
        verbose_name_plural = _("Application")


class Build(models.Model):

    #__Build_FIELDS__
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    #__Build_FIELDS__END

    class Meta:
        verbose_name        = _("Build")
        verbose_name_plural = _("Build")



#__MODELS__END
