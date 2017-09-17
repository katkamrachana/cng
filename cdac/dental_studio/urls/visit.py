from django.conf.urls import patterns, url

urlpatterns = patterns('cdac.dental_studio.views.visit',
                url(r'^/visit/(?P<visit_id>[0-9]+)/$', 'visit_detail', name='visit'),
                )

