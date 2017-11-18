from django.conf.urls import url
from dental_studio.views import appointment
app_name = 'appointment'
urlpatterns = [url(r'^(?P<appointment_id>[0-9]+)/$', appointment.appointment_detail, name='appointment'),
                url(r'^add', appointment.create_edit, name='create'),
                url(r'^edit/(?P<appointment_id>[0-9]+)$', appointment.create_edit, name='edit'),
				url(r'^data/$', appointment.load_table, name='laod_table'),
				url(r'^request/$', appointment.complete_booking, name='complete_booking'),

]
