# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def visit_detail(request, visit_id):
    response = "You're looking at the visit detail %s."
    return HttpResponse(response % visit_id)
