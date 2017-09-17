# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def treatment_detail(request, treatment_id):
    return HttpResponse("You're voting on treatment %s." % treatment_id)