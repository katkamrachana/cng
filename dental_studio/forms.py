from django import forms

from .models import *
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'contact', 'email', 'address', 'age', 'first_appointment_date', 'gender')
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        # fields = ('datetime', 'name', 'contact', 'email', 'address', 'age', 'treatment', 'gender')
        fields = ('datetime', 'name', 'contact', 'email', 'address', 'age', 'gender')

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('visited_date','comments','patient','treatment','appointment')

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ('name', 'description', 'cost')

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('name', 'email', 'title', 'content')
'''
class TreatmentForm(forms.ModelForm):
    treatment_description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Treatment
'''