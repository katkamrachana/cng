from django.conf.urls import patterns, url

urlpatterns = patterns('cdac.dental_studio.views.treatment',
                url(r'^/treatment/(?P<treatment_id>[0-9]+)/$', 'treatment_detail', name='treatment'),
                )
