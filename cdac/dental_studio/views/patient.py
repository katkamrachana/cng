# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def patient_detail(request, patient_id):
    return HttpResponse("You're voting on patient %s." % patient_id)