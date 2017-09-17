# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Appointment, Treatment, Visit, Patient
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Treatment)
admin.site.register(Visit)
