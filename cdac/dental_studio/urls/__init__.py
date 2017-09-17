from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include(cdac.dental_studio.urls.home)),
    url(r'^/appointment', include(cdac.dental_studio.urls.appointment)),
    url(r'^/visit', include(cdac.dental_studio.urls.visit)),
    url(r'^/treatment', include(cdac.dental_studio.urls.treatment)),
    url(r'^/patient', include(cdac.dental_studio.urls.patient)),
]
