from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from account.api import UserResource, AccountResource
from note.api import UserProfileResource, NoteBookResource, NoteResource, TagResource
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(AccountResource())
v1_api.register(UserProfileResource())
v1_api.register(NoteBookResource())
v1_api.register(NoteResource())
v1_api.register(TagResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xiangshare.views.home', name='home'),
    url(r'^accounts/', include('account.urls', namespace="account")),
    url(r'^note/', include('note.urls', namespace="note")),
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/', include(v1_api.urls)),
)
