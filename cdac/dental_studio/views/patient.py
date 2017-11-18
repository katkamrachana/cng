# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from dental_studio.forms import PatientForm
from dental_studio.models import *
from dental_studio.views.tables import *

def patient(request):
	print "\n\n1*************"
	pass

def patient_detail(request, patient_id):
    return HttpResponse("You're voting on patient %s." % patient_id)

def load_table(request):
    table = Patient.patients()
    return render(request, 'dental_studio/table.html', {'table': table})

def patient_delete(request, patient_id):
	pass


def patient_create_edit(request, patient_id=None):
	print "*"*80
	form = PatientForm()
	print form
	print "*"*80
	return render(request, 'dental_studio/node_create.html', {'form': form})

def patient_create(request):
	print "\nHELLo"
	pass


