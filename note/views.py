#coding: UTF-8
import time, datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core import serializers
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import json
from django.core.urlresolvers import reverse
from note.models import *

def notebook_list(request):
    user_id = request.GET.get("user")
    user = User.objects.get(id=user_id)
    userprofile = UserProfile.objects.filter(user=user).first()
    if userprofile:
        notebooks = NoteBook.objects.filter(userprofile=userprofile)
    else:
        notebooks=[]
    # notebooks = serializers.serialize("json", notebooks)
    # response = HttpResponse()
    # response['Content-Type'] = 'text/javascript'
    # response.write(notebooks)
    # return response

    variables = RequestContext(request, {
        'notebooks': notebooks,
        })
    return render_to_response('note/notebook_list.html', variables)

def notebook_detail(request):
    notebook_guid = request.GET.get("notebook")
    notebook = NoteBook.objects.get(guid=notebook_guid)
    notes = Note.objects.filter(notebook=notebook)
    variables = RequestContext(request, {
        'notes': notes,
        })
    return render_to_response('note/notebook_detail.html', variables)

def note_detail(request):
    note_guid = request.GET.get("note")
    note = Note.objects.get(guid=note_guid)
    variables = RequestContext(request, {
        'note': note,
        })
    return render_to_response('note/note_detail.html', variables)
    
@login_required
def main_page(request):
    variables = RequestContext(request, {

        })
    return render_to_response('note/main_page.html', variables)

