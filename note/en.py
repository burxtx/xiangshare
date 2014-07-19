import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient
# Create your views here.
auth_token = "S=s1:U=8ef64:E=14e6c6294c5:C=14714b165a0:P=1cd:A=en-devtoken:V=2:H=bf59286e0b0a5ae59e33b20dd11001f0"

def get_notebook_list():
    client = EvernoteClient(token=auth_token, sandbox=True)
    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()
    return notebooks

def get_note_list(notebook):
    if notebook:
        pass
    else:
        return 
