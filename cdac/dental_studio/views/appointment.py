# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from dental_studio.forms import AppointmentForm
# Create your views here.

def appointment_detail(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except appointment.DoesNotExist:
        raise Http404("appointment does not exist")
    return render(request, 'dental_studio/appointment.html', {'appointment': appointment})


def appointment_create_edit(request, appoinment_id=None):
	print "*"*80
	form = AppointmentForm()
	print form
	print "*"*80
	return render(request, 'dental_studio/node_create.html', {'form': form})
