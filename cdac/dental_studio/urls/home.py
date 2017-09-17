from django.conf.urls import patterns, url

urlpatterns = patterns('cdac.dental_studio.views.home',
                url(r'^', 'welcome', name='welcome'),
                )
