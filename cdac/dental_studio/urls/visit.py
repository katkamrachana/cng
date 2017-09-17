from django.conf.urls import url
from dental_studio.views import visit
urlpatterns = [url(r'^/visit/(?P<visit_id>[0-9]+)/$', visit.visit_detail, name='visit'),]

