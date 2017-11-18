from django.conf.urls import url
from dental_studio.views.patient import *
urlpatterns = [
                url(r'^$', patient, name='list'),
                url(r'^add', patient_create_edit, name='create'),
                url(r'^(?P<patient_id>[0-9]+)$', patient_detail, name='detail'),
                url(r'^(?P<patient_id>[0-9]+)/delete$', patient_delete, name='delete'),
				url(r'^data/$', load_table, name='laod_table'),
                # url(r'^(?P<patient_id>[0-9]+)/edit$', patient_create_edit, name='patient_edit'),
                ]
