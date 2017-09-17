from django.conf.urls import url
from dental_studio.views.patient import *
urlpatterns = [
                url(r'^$', patient, name='patient'),
                url(r'^add', patient_create_edit, name='patient_create'),
                url(r'^(?P<patient_id>[0-9]+)$', patient_detail, name='patient_detail'),
                url(r'^(?P<patient_id>[0-9]+)/delete$', patient_delete, name='patient_delete'),
                # url(r'^(?P<patient_id>[0-9]+)/edit$', patient_create_edit, name='patient_edit'),
                ]
