from django.conf.urls import url
from dental_studio.views.visit import *
app_name = 'visit'
urlpatterns = [url(r'^(?P<visit_id>[0-9]+)/$', visit_detail, name='visit'),
				url(r'^add', visit_create_edit, name='create'),
				url(r'^data/$', load_table, name='laod_table'),
				]

