# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
# Create your models here.


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=6,default='baby')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Img(models.Model):
    img = models.ImageField(upload_to='upload')
    tag = models.ForeignKey(Tag)

    def __str__(self):
        return self.img

    def get_absolute_url(self):
        return reverse('img:uploadpage')