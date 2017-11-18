from django.conf.urls import url, include
from dental_studio.views.patient import *
from dental_studio.views import home

urlpatterns = [
    url(r'^$', home.welcome, name='welcome'),
	url(r'^management', home.management, name='management'),
	url(r'^dashboard', home.dashboard, name='laod_dashboard'),
    url(r'^appointment/', include('dental_studio.urls.appointment', namespace='appointment')),
    url(r'^visit/', include('dental_studio.urls.visit', namespace='visit')),
    url(r'^treatment/', include('dental_studio.urls.treatment', namespace='treatment')),
    url(r'^patient/', include('dental_studio.urls.patient', namespace='patient')),
    url(r'^testimonial/', include('dental_studio.urls.testimonial', namespace='testimonial')),
]
