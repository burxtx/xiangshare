#coding: UTF-8
import evernote.edam.userstore.constants as UserStoreConstants
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

import enml2html as enml
from note.models import *

# Create your views here.
# dev_token = "S=s2:U=79814:E=1519ceed452:C=14a453da6e0:P=1cd:A=en-devtoken:V=2:H=74a39fb5a42851e8796f4aad96c1d9ca"
dev_token = "S=s1:U=901bc:E=151e898fd39:C=14a90e7d098:P=1cd:A=en-devtoken:V=2:H=f0474393308a439da0c49e2c594e795e"
# client = EvernoteClient(token=dev_token)
# userStore = client.get_user_store()
# user = userStore.getUser()
# notestore = client.get_note_store()
# notebooks = notestore.listNotebooks()
# # notebooks = notestore.listSharedNotebooks()
result_spec = NotesMetadataResultSpec(includeTitle=True)
# for n in notebooks:
#     # print type(n)
#     print n.name
#     # print n.guid
#     notefilter = NoteFilter(notebookGuid=n.guid)
#     notes = notestore.findNotesMetadata(dev_token, notefilter, 0, 5, result_spec)
#     for note in notes.notes:
#         print note.title
#         print note.guid
#         # content = notestore.getNote(dev_token, note.guid, True, False, False, False)
#         content = notestore.getNoteContent(note.guid)
#         print content
# # print user.username

def sync(request, notestore):
    notebooks = notestore.listNotebooks()
    userprofile, created = UserProfile.objects.get_or_create(user=request.user)
    for nb in notebooks:
        notebook, created = NoteBook.objects.get_or_create(guid=nb.guid)
        notebook.guid = nb.guid
        notebook.name = nb.name
        notebook.userprofile = userprofile
        notebook.save()

        notefilter = NoteFilter(notebookGuid=nb.guid)
        notes = notestore.findNotesMetadata(notefilter, 0, 5, result_spec)
        for n in notes.notes:
            mediastore = enml.FileMediaStore(notestore, n.guid, '/c/note-resources/')
            content = notestore.getNoteContent(n.guid)
            content = enml.ENMLToHTML(content, False, media_store=mediastore)
            note, created = Note.objects.get_or_create(guid=n.guid)
            note.guid = n.guid
            note.title = n.title
            note.notebook = notebook
            note.content = content
            # note.tag = 
            note.save()
