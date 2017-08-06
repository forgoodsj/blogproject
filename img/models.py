# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
from django.contrib import admin
# Create your models here.


#@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

#@python_2_unicode_compatible
class Img(models.Model):
    tag = models.ForeignKey('Tag')
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='upload')
    caption = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return self.img.url

    def get_absolute_url(self):
        return reverse('img:upload')

