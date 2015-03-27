from django.shortcuts import render,redirect
from django.http import HttpResponse
from replay.forms import *
from replay.models import *
from user.helper import *
from user.decorators import *
from copy import deepcopy

# Create your views here.
def listReplay(Request):
    replays = Replay.objects.all()
    return render(Request, "listreplay.html", {'replays': replays})

@login_required
def addReplay(request):
    if request.method == 'POST' :
        form = ReplayForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/replay')
    else :
        form = ReplayForm()

    return render(request,'replayform.html',{'form':form})

# @same_user_or_admin_required
@login_required
def editReplay(request,id):
    user = get_user(request)
    try:
        replay = Replay.objects.get(pk=id)
    except:
        return render(request,'error.html',{'msg':'Replay Not Found', 'user1': user})


    if not (user.id == replay.author.id or user.role == 'a'):
        return render(request,'error.html',{'msg':'You Must Be The Author or the admin', 'user1': user})

    if request.method == 'POST' :
        data = deepcopy(request.POST)
        data['author'] = replay.author.id
        data['mythread'] = replay.thread.id
        form = ReplayForm(data=data,instance=replay)
        # del form.fields['password']
        if form.is_valid():
            form.save()
            return redirect('/thread/list/'+str(replay.thread.id))
    else :
        form = ReplayForm(instance=replay)
        del form.fields['author']
        del form.fields['mythread']


    return render(request,'replayform.html',{'form':form})


# @same_user_or_admin_required
@login_required
def delReplay(request,id,replay_id):
    user = get_user(request)
    try:
        replay = Replay.objects.get(pk=replay_id)
        thread_id = replay.thread.id

        if not (user.id == replay.author.id or user.role == 'a'):
            return render(request,'error.html',{'msg':'You Must Be The Author or the admin', 'user1': user})

        replay.delete()

    except Replay.DoesNotExist:
        return render(request,'error.html',{'msg':'Replay Not Found', 'user1': user})

    return redirect('/thread/list/'+str(thread_id))
