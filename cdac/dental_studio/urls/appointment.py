from django.conf.urls import url
from dental_studio.views import appointment
urlpatterns = [url(r'^/appointment/(?P<appointment_id>[0-9]+)/$', appointment.appointment_detail, name='appointment')]