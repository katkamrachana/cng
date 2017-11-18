from django.conf.urls import url
from dental_studio.views.testimonial import *
app_name = 'testimonial'
urlpatterns = [url(r'^(?P<testimonial_id>[0-9]+)/$', testimonial_detail, name='testimonial'),
				url(r'^add', testimonial_create_edit, name='create'),
				url(r'^data/$', load_table, name='laod_table'),
				]

