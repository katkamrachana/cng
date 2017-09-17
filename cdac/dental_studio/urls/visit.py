from django.conf.urls import url
from dental_studio.views import visit
app_name = 'visit'
urlpatterns = [url(r'^(?P<visit_id>[0-9]+)/$', visit.visit_detail, name='visit'),]

