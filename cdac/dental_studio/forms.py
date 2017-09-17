from django import forms

from .models import *
class PatientForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'contact', 'email', 'address', 'age', 'first_appointment_date', 'gender')

'''
class VisitForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Visit

class AppointmentForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Appointment


class TreatmentForm(forms.ModelForm):
    treatment_description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Treatment
'''