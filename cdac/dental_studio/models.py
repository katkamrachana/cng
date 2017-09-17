# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django import forms

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30, unique=True, blank=False)
    last_name = models.CharField(max_length=30, unique=True, blank=False)
    contact = models.CharField(max_length=12, unique=True, blank=False)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300, blank=False)
    age = models.IntegerField(default=0, blank=False)
    first_appointment_date = models.DateTimeField('Registration Date')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def patients(self):
        """Return the list of all Patients."""
        return Patient.objects.all()


class PatientAdmin(admin.ModelAdmin):
    raw_id_fields = ('first_name','last_name') 
    search_fields = ('first_name', 'last_name')
    list_display = ('__unicode__', 'contact', 'address', 'email', 'age' )

class Treatment(models.Model):
    treatment_name = models.CharField(max_length=200, unique=True, blank=False)
    treatment_description = models.CharField(max_length=500)
    treatment_cost = models.IntegerField(default=0, blank=False)

    def __unicode__(self):
        return self.treatment_name



class Appointment(models.Model):
    datetime = models.DateTimeField('Appointment date')
    name = models.CharField(max_length=50, unique=True, blank=False)
    contact = models.CharField(max_length=12, unique=True, blank=False)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300, blank=False)
    age = models.IntegerField(default=0, blank=False)
    treatment = models.ForeignKey(Treatment)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __unicode__(self):
        return '%s (%s) - %s' % (self.name, self.contact, self.datetime)

class Visit(models.Model):
    visited_date = models.DateTimeField(blank=False)
    comments = models.CharField(max_length=2000)
    patient = models.ForeignKey(Patient, blank=False)
    treatment = models.ForeignKey(Treatment, blank=False)
    appointment = models.ForeignKey(Appointment, blank=False)

    def __unicode__(self):
        return '%s - %s' % (self.patient.first_name, self.visited_date)

class Testimonial(models.Model):
    content = models.CharField(max_length=2000)
    created_date = models.DateTimeField()
    user = models.CharField(max_length=50, unique=True)

