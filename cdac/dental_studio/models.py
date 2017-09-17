# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django import forms

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    contact = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=300)
    age = models.IntegerField(default=0)
    first_appointment_date = models.DateTimeField('Registration Date')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class PatientAdmin(admin.ModelAdmin):
    raw_id_fields = ('first_name','last_name') 
    search_fields = ('first_name', 'last_name')
    list_display = ('__unicode__', 'contact', 'address', 'email', 'age' )

class Treatment(models.Model):
    treatment_name = models.CharField(max_length=200, unique=True)
    treatment_description = models.CharField(max_length=500)
    treatment_cost = models.IntegerField(default=0)

    def __unicode__(self):
        return self.treatment_name



class Appointment(models.Model):
    datetime = models.DateTimeField('Appointment date')
    name = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=300)
    age = models.IntegerField(default=0)
    treatment = models.ForeignKey(Treatment)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __unicode__(self):
        return '%s (%s) - %s' % (self.name, self.contact, self.datetime)

class Visit(models.Model):
    visited_date = models.DateTimeField()
    comments = models.CharField(max_length=2000)
    patient = models.ForeignKey(Patient)
    treatment = models.ForeignKey(Treatment)
    appointment = models.ForeignKey(Appointment)

    def __unicode__(self):
        return '%s - %s' % (self.patient.first_name, self.visited_date)

class Testimonial(models.Model):
    content = models.CharField(max_length=2000)
    created_date = models.DateTimeField()
    user = models.CharField(max_length=50, unique=True)
'''
class VisitForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Visit

class AppointmentForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Appointment

class PatientForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Patient

class TreatmentForm(forms.ModelForm):
    treatment_description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Treatment
'''