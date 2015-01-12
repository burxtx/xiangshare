#coding: UTF-8
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from note.models import UserProfile, NoteBook, Note, Tag


class UserProfileResource(ModelResource):
    class Meta(object):
        queryset = UserProfile.objects.all()
        resource_name = 'userprofile'

class NoteBookResource(ModelResource):
    userprofile = fields.ToOneField(UserProfileResource, 'userprofile')
    class Meta(object):
        queryset = NoteBook.objects.all()
        resource_name = 'notebook'

class NoteResource(ModelResource):
    class Meta(object):
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()

class TagResource(ModelResource):
    class Meta(object):
        queryset = Tag.objects.all()
        resource_name = 'tag'