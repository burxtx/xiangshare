#coding: UTF-8
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views, oauth

urlpatterns = patterns('',
    url(r"^auth/$", oauth.auth, name="evernote_auth"),
    url(r"^callback/$", oauth.callback, name="evernote_callback"),
    url(r"^reset/$", oauth.reset, name="evernote_auth_reset"),

    url(r"^$", views.main_page, name="main_page"),
    url(r'^notebook-list/$', views.notebook_list, name="notebook_list"),
    url(r'^notebook-detail/$', views.notebook_detail, name="notebook_detail"),
    url(r'^note-detail/$', views.note_detail, name="note_detail"),
)