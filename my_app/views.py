# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from my_app.models import Device

# Create your views here.

def index(request):
    devices = Device.objects.new()
    return render(request, 'index.html', {'devices' : devices })