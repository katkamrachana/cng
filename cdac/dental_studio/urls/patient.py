from django.conf.urls import patterns, url

urlpatterns = patterns('cdac.dental_studio.views.patient',
                    url(r'^/patient/(?P<patient_id>[0-9]+)/$', 'patient_detal', name='patient'),
                )

