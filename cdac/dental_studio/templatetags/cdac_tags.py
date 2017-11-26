from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from dental_studio.models import *
from django.template import Library
import json

register = Library()

@register.assignment_tag
def get_testimonials():
    t = Testimonial.testimonials()
    return t

@register.inclusion_tag('dental_studio/add_testimonial.html', takes_context=True)
def add_testimonials():
    print "\nHERE"
    return {"HERE": "HELLO"}

@register.assignment_tag
def get_form(form_name):
    from dental_studio.forms import TestimonialForm
    form = TestimonialForm()
    return form

@register.assignment_tag
def get_testimonial_emails():
    all_emails = Testimonial.get_email_list()
    print "\n AALL EMAILS: ", all_emails
    return all_emails