from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.simple_response, name='simple_response'),
]