from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^login$', views.login),
    url(r'^signin$', views.signin),
    url(r'^signin_django$', views.signin_django),
    url(r'^about$', views.about),
    url(r'^consumer$', views.consumer),
    url(r'^merchant$', views.merchant),
    url(r'^list$', views.list),
    url(r'^product$', views.product),
    url(r'^tender$', views.tender),

]