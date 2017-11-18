# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from dental_studio.models import *
# Create your views here.

def welcome(request):
    # return HttpResponse("Welcome message..")
    template = loader.get_template('dental_studio/homepage.html')
    context = {
        'title': "Welcome"
    }
    return HttpResponse(template.render(context, request))


def management(request):
    # return HttpResponse("Welcome message..")
    return HttpResponseRedirect(reverse('laod_dashboard'))
    # template = loader.get_template('dental_studio/management.html')
    # context = {
    #     'title': "Manage Information System"
    # }
    # return HttpResponse(template.render(context, request))

def dashboard(request):
    # check for super user status
    patients_cur = Patient.patients()
    patients_count = len(patients_cur)

    appointments_cur = Appointment.appointments()
    appointments_count = len(appointments_cur)

    treatments_cur = Treatment.treatments()
    treatments_count = len(treatments_cur)

    visits_cur = Visit.visits()
    visits_count = len(visits_cur)

    testimonials_cur = Testimonial.testimonials()
    testimonials_count = len(testimonials_cur)


    context = {
        'title': "General Dashboard of CDAC",
        "patients_cur": patients_cur,
        "patients_count": patients_count,
        "appointments_cur": appointments_cur,
        "appointments_count": appointments_count,
        "treatments_cur": treatments_cur,
        "treatments_count": treatments_count,
        "visits_cur": visits_cur,
        "visits_count": visits_count,
        "testimonials_cur": testimonials_cur,
        "testimonials_count": testimonials_count
    }
    return render(request, 'dental_studio/dashboard.html', context)

