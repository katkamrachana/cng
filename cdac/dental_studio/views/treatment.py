# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from dental_studio.forms import TreatmentForm
from dental_studio.models import *
from dental_studio.views.tables import *

def treatment_detail(request, treatment_id):
    return HttpResponse("You're voting on treatment %s." % treatment_id)

def load_table(request):
    table = Treatment.treatments()
    return render(request, 'dental_studio/table.html', {'table': table})

def treatment_create_edit(request, appoinment_id=None):
	print "*"*80
	form = TreatmentForm()
	print form
	print "*"*80
	return render(request, 'dental_studio/node_create.html', {'form': form})
