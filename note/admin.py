from django.contrib import admin
from note.models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(NoteBook)
admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(NoteTag)
