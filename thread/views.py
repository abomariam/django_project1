from django.shortcuts import render,redirect
from django.http import HttpResponse
from thread.forms import *
from thread.models import *
from user.helper import *
from copy import deepcopy
from replay.forms import *
from user.helper import *
from user.decorators import *


def list_replies(request, id):
    try:
        thread = Thread.objects.get(pk=id)
    except:
        return HttpResponse("Thread Doesn't Exist")

    form = ReplayForm()
    del form.fields['author']
    del form.fields['thread']

    if request.method == 'POST':
        data = deepcopy(request.POST)
        data['author'] = get_user(request).id
        data['thread'] = id

        form = ReplayForm(data=data)
        if form.is_valid():
            form.save()
            return redirect('/thread/list/'+str(id))
        else:
            del form.fields['author']
            del form.fields['thread']

    return render(request,'list_replays.html',{'thread':thread,'form':form, 'user1':get_user(request)})


# Create your views here.
def listThread(Request):
    threads = Thread.objects.all()
    return render(Request, "listthread.html", {'threads': threads})

@login_required
def addThread(request,forum_id):
    user = get_user(request)
    try:
        Forum.objects.get(pk=forum_id)
    except:
        return HttpResponse("Wrong Forum")

    if request.method == 'POST' :
        data = deepcopy(request.POST)
        data['author'] = user.id
        data['forum'] = forum_id
        if user.role != 'a':
            data['sticky'] = False
            data['lock'] = False
        form = ThreadForm(data=data)

        if form.is_valid():
            form.save()
            return redirect('/forum/list/'+str(forum_id))
    else :
        form = ThreadForm()
        del form.fields['author']
        del form.fields['forum']
        if user.role != 'a':
            del form.fields['sticky']
            del form.fields['lock']


    return render(request,'threadform.html',{'form':form, 'user1':get_user(request)})

# @same_user_or_admin_required
@login_required
def editThread(request,id):
    user = get_user(request)
    try:
        thread = Thread.objects.get(pk=id)
    except:
        return HttpResponse("thread Not Found")

    if not (user.id == thread.author.id or user.role == 'a'):
        return render(request,'error.html',{'msg':'You Must Be The Author or the admin', 'user1': user})

    if request.method == 'POST' :
        data = deepcopy(request.POST)
        data['author'] = thread.author.id
        data['forum'] = thread.forum.id
        if user.role != 'a':
            data['sticky'] = False
            data['lock'] = False

        form = ThreadForm(data=data,instance=thread)
        # del form.fields['password']
        if form.is_valid():
            form.save()
            return redirect('/thread/list/'+str(thread_id))
    else :
        form = ThreadForm(instance=thread)
        del form.fields['author']
        del form.fields['forum']
        if user.role != 'a':
            del form.fields['sticky']
            del form.fields['lock']


    return render(request,'threadform.html',{'form':form})


# @same_user_or_admin_required
@login_required
def delThread(request,id):
    user = get_user()
    try:
        thread = Thread.objects.get(pk=id)
        if not (user.id == thread.author.id or user.role == 'a'):
            return render(request,'error.html',{'msg':'You Must Be The Author or the admin', 'user1': user})

        forum_id = thread.forum.id
        thread.delete()
        return redirect('/forum/list/'+str(forum_id))
    except Thread.DoesNotExist:
        return HttpResponse('Not found')


