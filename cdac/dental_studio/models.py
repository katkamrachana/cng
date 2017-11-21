# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib import admin
from django import forms
from django.utils import timezone

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

    @staticmethod
    def patients():
        """Return the list of all Patients."""
        return Patient.objects.all()

class PatientAdmin(admin.ModelAdmin):
    raw_id_fields = ('first_name','last_name') 
    search_fields = ('first_name', 'last_name')
    list_display = ('__unicode__', 'contact', 'address', 'email', 'age' )



class Treatment(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    description = models.CharField(max_length=500)
    cost = models.IntegerField(default=0, blank=False)

    def __unicode__(self):
        return self.name

    @staticmethod
    def treatments():
        """Return the list of all Patients."""
        return Treatment.objects.all()



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

    @staticmethod
    def appointments():
        """Return the list of all Patients."""
        return Appointment.objects.all()

    # def clean_date(self):
    #     date = self.cleaned_data['datetime']
    #     if date < datetime.date.today():
    #         raise forms.ValidationError("The date cannot be in the past!")
    #     return date


class Visit(models.Model):
    visited_date = models.DateTimeField(blank=False)
    comments = models.CharField(max_length=2000)
    patient = models.ForeignKey(Patient, blank=False)
    treatment = models.ForeignKey(Treatment, blank=False)
    appointment = models.ForeignKey(Appointment, blank=False)

    def __unicode__(self):
        return '%s - %s' % (self.patient.first_name, self.visited_date)

    @staticmethod
    def visits():
        """Return the list of all Patients."""
        return Visit.objects.all()


class Testimonial(models.Model):
    title = models.CharField(max_length=40, blank=False, default='')
    content = models.CharField(max_length=2000, blank=False, default='')
    created_date = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D')
    email = models.EmailField(unique=True, default='')

    @staticmethod
    def testimonials():
        """Return the list of all Patients."""
        return Testimonial.objects.all()

