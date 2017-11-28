# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from dental_studio.forms import VisitForm
from dental_studio.models import *
from dental_studio.views.tables import *

def visit_detail(request, visit_id):
    response = "You're looking at the visit detail %s."
    return HttpResponse(response % visit_id)


def load_table(request):
    # table = AppointmentTable(Appointment.appointments())
    # RequestConfig(request).configure(table)
    table = Visit.visits()
    return render(request, 'dental_studio/table.html', {'table': table})


def visit_create_edit(request, appoinment_id=None):
	print ("*"*80)
	form = VisitForm()
	print (form)
	print ("*"*80)
	return render(request, 'dental_studio/node_create.html', {'form': form})
