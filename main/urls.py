from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^login$', views.login),
    url(r'^signin$', views.signin),
    url(r'^about$', views.about),

]