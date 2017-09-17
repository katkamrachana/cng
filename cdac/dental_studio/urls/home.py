from django.conf.urls import url
from dental_studio.views import home
urlpatterns = [url(r'^', home.welcome, name='welcome'),]
