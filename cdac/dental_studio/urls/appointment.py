from django.conf.urls import patterns, url

urlpatterns = patterns('cdac.dental_studio.views.appointment',
                url(r'^/appointment/(?P<appointment_id>[0-9]+)/$', 'appointment_detail', name='appointment'),
                )