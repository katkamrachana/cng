# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def appointment_detail(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except appointment.DoesNotExist:
        raise Http404("appointment does not exist")
    return render(request, 'dental_studio/appointment.html', {'appointment': appointment})
