from django.conf.urls import url
from dental_studio.views import treatment
urlpatterns = [url(r'^/treatment/(?P<treatment_id>[0-9]+)/$', treatment.treatment_detail, name='treatment'),]
