# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Img(models.Model):
    img = models.ImageField(upload_to='upload')
    tag = models.IntegerField(max_length=6)