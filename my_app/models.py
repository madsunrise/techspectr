# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime




class DeviceManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	def cheaper(self):
		return self.order_by('price')
	def expensive(self):
		return self.order_by('-price')


class Device(models.Model):
	title = models.CharField (max_length = 128)
	description = models.TextField()
	added_at = models.DateTimeField(default = datetime.datetime.now)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	objects = DeviceManager()
