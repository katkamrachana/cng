# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def welcome(request):
    # return HttpResponse("Welcome message..")
    template = loader.get_template('dental_studio/onepage.html')
    context = {
        'title': "Welcome"
    }
    return HttpResponse(template.render(context, request))


def management(request):
    # return HttpResponse("Welcome message..")
    template = loader.get_template('dental_studio/management.html')
    context = {
        'title': "Manage Information System"
    }
    return HttpResponse(template.render(context, request))

