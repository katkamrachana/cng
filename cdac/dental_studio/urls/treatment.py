from django.conf.urls import url
from dental_studio.views.treatment import * 
app_name = 'treatment'
urlpatterns = [url(r'^(?P<treatment_id>[0-9]+)/$', treatment_detail, name='treatment'),
					url(r'^add', treatment_create_edit, name='create'),]
