# coding: UTF-8
from django.http import Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from account.forms import *
from account.models import *
# import pdb
# pdb.set_trace()

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def login_page(request):
    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return login(request)

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                )
            Account.objects.create(user=user)
            return HttpResponseRedirect(reverse('account:register_success'))
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form':form
        })
    return render_to_response('registration/register.html', variables)

@login_required
def account_page(request):
    print request.user.username
    account = Account.objects.filter(user=request.user).first()
    form = AccountForm({
        'username': account.user.username,
        'introduction': account.introduction,
        'avatar': account.avatar,
        })
    print form
    print account.avatar
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            # user = User.objects.get(username=form.cleaned_data['username'])
            # print user.username
            username = form.cleaned_data["username"]
            introduction = form.cleaned_data["introduction"]
            avatar = form.cleaned_data["avatar"]
            user = request.user
            print username
            account = Account.objects.filter(user=request.user).first()
            if account:
                print 'ififif'
                user.username = username
                user.save()
                account.introduction = introduction
                account.avatar = avatar
            else:
                print 'elelel'
                user.username = username
                user.save()
                account = Account.objects.create(
                    user = user,
                    avatar=avatar,
                    introduction=introduction,
                    )
            account.save()
            return HttpResponseRedirect(reverse('note:notebook_list', args=[request.user.username]))
    
    variables = RequestContext(request, {
        'form':form
        })
    return render_to_response('account/account.html', variables)
    