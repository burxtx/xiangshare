#coding: UTF-8
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('account.views',
    url(r'^profile/$', 'account_page', name="account_page"),
    url(r'^login/$', 'login_page', name="login_page"),
    url(r'^logout/$', 'logout_page', name="logout_page"),
    url(r'^register/$', 'register_page', name="register_page"),
    url(r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html'), name="register_success"),
)