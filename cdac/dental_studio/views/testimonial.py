# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.urls import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from dental_studio.forms import TestimonialForm
from dental_studio.models import *
from dental_studio.views.tables import *

def testimonial_detail(request, testimonial_id):
    response = "You're looking at the testimonial detail %s."
    return HttpResponse(response % testimonial_id)


def load_table(request):
    # table = AppointmentTable(Appointment.appointments())
    # RequestConfig(request).configure(table)
    table = Testimonial.testimonials()
    return render(request, 'dental_studio/table.html', {'table': table})


def create_edit(request, testimonial_id=None):
    print "*"*80
    args = {}
    # set_date = True
    if testimonial_id:
        testimonial_obj = Testimonial.get.object(pk=testimonial_id)
        # set_date = False
    if request.method == 'POST':
        print "\nrequest.POST: ", request.POST
        form = TestimonialForm(request.POST)
        print "\nPOST: form: ", form.errors
        if form.is_valid():
            try:
                testimonial_obj = form.save()
                testimonial_id = testimonial_obj.pk
                # if set_date:
                #     testimonial_obj.created_date = datetime.datetime.now()
                if request.user.is_superuser:
                    testimonial_obj.status = "P"
                # print "\n instance: ", new_appt.pk
                return HttpResponseRedirect(reverse('appointment:complete_booking'))
            except Exception as e:
                print "\n\ne: ", e
                # raise e
                pass
    else:
        form = TestimonialForm()
        args['form'] = form
        print form
    print "*"*80
    return render(request, 'dental_studio/node_create.html', {'form': form, 'action_url': 'testimonial:create', 'title': "Write Testimonial"}, args)
