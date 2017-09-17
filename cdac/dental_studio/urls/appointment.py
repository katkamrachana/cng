from django.conf.urls import url
from dental_studio.views import appointment
app_name = 'appointment'
urlpatterns = [url(r'^(?P<appointment_id>[0-9]+)/$', appointment.appointment_detail, name='appointment')]