from django.conf.urls import url
from dental_studio.views import patient
urlpatterns = [url(r'^/patient/(?P<patient_id>[0-9]+)/$', patient.patient_detail, name='patient'),]
