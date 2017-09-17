from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.welcome, name='welcome'),
	url(r'^/appointment/(?P<appointment_id>[0-9]+)/$', views.appointment_detail, name='appointment'),
    url(r'^/visit/(?P<visit_id>[0-9]+)/$', views.visit_detail, name='visit'),
    url(r'^/treatment/(?P<treatment_id>[0-9]+)/$', views.treatment_detail, name='treatment'),
]
