import django_tables2 as tables
from dental_studio.models import *

class PatientTable(tables.Table):
    class Meta:
        model = Patient
        template = 'dental_studio/table.html'

class TreatmentTable(tables.Table):
    class Meta:
        model = Treatment
        template = 'dental_studio/table.html'

class AppointmentTable(tables.Table):
    class Meta:
        model = Appointment
        template = 'dental_studio/table.html'

class VisitTable(tables.Table):
    class Meta:
        model = Visit
        template = 'dental_studio/table.html'

class TestimonialTable(tables.Table):
    class Meta:
        model = Testimonial
        template = 'dental_studio/table.html'
