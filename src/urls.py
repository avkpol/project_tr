"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from project_tr.views.control_v import ControlUpdateView



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "src.project_tr.views.control_v.index", name ='home'),
    url(r'^controls_list', "src.project_tr.views.control_v.controls_list", name = 'controls_list'),
    # url(r'^controls_list/control_edit_form', ControlUpdateView.as_view(), name = 'control_edit_form')
    # url(r'^control_edit_form', "src.project_tr.views.control_v.control_edit_form", name = 'control_edit_form')
    url(r'^control_edit_form/(?P<pk>\d+)/$',ControlUpdateView.as_view(),name = 'control_edit_form'),



]
