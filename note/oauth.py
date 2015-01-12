from evernote.api.client import EvernoteClient
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from wrapper import sync

EN_CONSUMER_KEY = 'tianxicool-5701'
EN_CONSUMER_SECRET = 'b15df0a549471701'


def get_evernote_client(token=None):
    if token:
        return EvernoteClient(token=token, sandbox=True)
    else:
        return EvernoteClient(
            consumer_key=EN_CONSUMER_KEY,
            consumer_secret=EN_CONSUMER_SECRET,
            sandbox=True
        )

def auth(request):
    client = get_evernote_client()
    callbackUrl = 'http://%s%s' % (
        request.get_host(), reverse('note:evernote_callback'))
    request_token = client.get_request_token(callbackUrl)
    # Save the request token information for later
    request.session['oauth_token'] = request_token['oauth_token']
    request.session['oauth_token_secret'] = request_token['oauth_token_secret']

    # Redirect the user to the Evernote authorization URL
    return redirect(client.get_authorize_url(request_token))


def callback(request):
    try:
        client = get_evernote_client()
        client.get_access_token(
            request.session['oauth_token'],
            request.session['oauth_token_secret'],
            request.GET.get('oauth_verifier', '')
        )
    except KeyError:
        return redirect(reverse('note:main_page'))

    note_store = client.get_note_store()
    sync(request, note_store)
    return HttpResponseRedirect(reverse('note:notebook_list')+"?user="+str(request.user.id))


def reset(request):
    return redirect('/')
