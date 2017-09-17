from django.conf.urls import url, include
from dental_studio.views.patient import *
from dental_studio.views import home

urlpatterns = [
    url(r'^$', home.welcome, name='welcome'),
    url(r'^appointment/', include('dental_studio.urls.appointment')),
    url(r'^visit/', include('dental_studio.urls.visit')),
    url(r'^treatment/', include('dental_studio.urls.treatment')),
    url(r'^patient/', include('dental_studio.urls.patient', namespace='patient')),
]
