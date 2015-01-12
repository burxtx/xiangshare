# coding: UTF-8
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """docstring for UserProfile"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True, related_name="user_userprofile")
    def __unicode__(self):
        return self.user.user
        
class NoteBook(models.Model):
    """docstring for NoteBook"""
    guid = models.CharField(max_length=100, null=True, blank=True, verbose_name="笔记本Guid")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="笔记本")
    create_time = models.DateTimeField(auto_now_add=True)
    userprofile = models.ForeignKey(UserProfile, null=True, blank=True)
    def __unicode__(self):
        return self.name

class Note(models.Model):
    """docstring for Note"""
    guid = models.CharField(max_length=100, null=True, blank=True, verbose_name="笔记Guid")
    notebook = models.ForeignKey(NoteBook, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name="标题")
    content = models.TextField(null=True, blank=True, verbose_name="内容")
    tag = models.CharField(max_length=20, null=True, blank=True, verbose_name="标签")
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    """docstring for Tag"""
    guid = models.CharField(max_length=100, null=True, blank=True, verbose_name="标签Guid")
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="标签")
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class NoteTag(models.Model):
    """docstring for NoteTag"""
    note = models.ForeignKey(Note, null=True, blank=True, verbose_name="笔记")
    tag = models.ForeignKey(Tag, null=True, blank=True, verbose_name="标签")

    def __unicode__(self):
        return self.note.title, self.tag.name