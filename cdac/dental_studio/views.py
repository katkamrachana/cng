# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def welcome(request):
    # return HttpResponse("Welcome message..")
    template = loader.get_template('dental_studio/homepage.html')
    context = {
        'title': "Welcome"
    }
    return HttpResponse(template.render(context, request))

def appointment_detail(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except appointment.DoesNotExist:
        raise Http404("appointment does not exist")
    return render(request, 'dental_studio/appointment.html', {'appointment': appointment})



def visit_detail(request, visit_id):
    response = "You're looking at the visit detail %s."
    return HttpResponse(response % visit_id)

def treatment_detail(request, treatment_id):
    return HttpResponse("You're voting on treatment %s." % treatment_id)