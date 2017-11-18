# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from dental_studio.forms import AppointmentForm
from dental_studio.models import *
from dental_studio.views.tables import *

def appointment_detail(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except appointment.DoesNotExist:
        raise Http404("appointment does not exist")
    return render(request, 'dental_studio/appointment.html', {'appointment': appointment})

def load_table(request):
    # table = AppointmentTable(Appointment.appointments())
    # RequestConfig(request).configure(table)
    table = Appointment.appointments()
    return render(request, 'dental_studio/table.html', {'table': table})


def create_edit(request, appoinment_id=None):
    print "*"*80
    args = {}
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        print "\nPOST: form: ", form.errors
        if form.is_valid():
            try:
                new_appt = form.save()
                print "\n instance: ", new_appt.pk
                return HttpResponseRedirect(reverse('appointment:complete_booking'))
            except Exception as e:
                print "\n\ne: ", e
                # raise e
                pass

    else:
        form = AppointmentForm()
        args['form'] = form
        print form
    print "*"*80
    return render(request, 'dental_studio/node_create.html', {'form': form, 'action_url': 'appointment:create'}, args)

def complete_booking(request):
    template = loader.get_template('dental_studio/booking_complete.html')
    context = {
        'title': "Appoinment Booking Request"
    }
    return HttpResponse(template.render(context, request))
