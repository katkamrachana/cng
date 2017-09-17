from django.conf.urls import url
from dental_studio.views import treatment
app_name = 'treatment'
urlpatterns = [url(r'^(?P<treatment_id>[0-9]+)/$', treatment.treatment_detail, name='treatment'),]
