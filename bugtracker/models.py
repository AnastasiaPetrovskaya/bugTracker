# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Ticket(models.Model):
    title = models.CharField(max_length = 128)
    text = models.TextField()
    created = models.DateTimeField(auto_now = True)
    closed = models.BooleanField(default = False)
    user = models.ForeignKey(User,)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
