from django.conf.urls import include, url
from . import views
import django.contrib.auth.views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^login$', views.do_login),
    url(r'^signin$', views.signin),
    url(r'^signin_django$', views.signin_django),
    url(r'^about$', views.about),
    url(r'^consumer$', views.consumer),
    url(r'^merchant$', views.merchant),
    url(r'^merchant_signin$', views.merchant_signin),
    url(r'^list$', views.list),
    url(r'^product$', views.product),
    url(r'^tender$', views.tender),
    url(r'^notification$', views.notification),
    url(r'^logout$', django.contrib.auth.views.logout, name ='logout', kwargs = {'next_page':'/ff/home'}),

]