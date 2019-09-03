# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Main(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    exception_type = models.CharField(max_length=100, blank=True, default='')
    exception_string = models.CharField(max_length=100, blank=True, default='')
    exception_repr = models.CharField(max_length=100, blank=True, default='')
    exception_args = models.CharField(max_length=100, blank=True, default='')
    exception_traceback = models.CharField(max_length=1000, blank=True, default='')

    class Meta:
        ordering = ['created']