from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('dental_studio.urls.home')),
    url(r'^/appointment', include('dental_studio.urls.appointment')),
    url(r'^/visit', include('dental_studio.urls.visit')),
    url(r'^/treatment', include('dental_studio.urls.treatment')),
    url(r'^/patient', include('dental_studio.urls.patient')),
]
