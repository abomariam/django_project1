from django.shortcuts import render,redirect
from django.http import HttpResponse
from replay.forms import *
from replay.models import *
from user.helper import *
from copy import deepcopy

# Create your views here.
def listReplay(Request):
    replays = Replay.objects.all()
    return render(Request, "listreplay.html", {'replays': replays})

def addReplay(request):
    if request.method == 'POST' :
        form = ReplayForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/replay')
    else :
        form = ReplayForm()

    return render(request,'replayform.html',{'form':form})

def editReplay(request,id):
    user = get_user(request)
    try:
        replay = Replay.objects.get(pk=id)
    except:
        return HttpResponse("replay Not Found")

    if request.method == 'POST' :
        data = deepcopy(request.POST)
        data['author'] = replay.author.id
        data['thread'] = replay.thread.id
        form = ReplayForm(data=data,instance=replay)
        # del form.fields['password']
        if form.is_valid():
            form.save()
            return redirect('/thread/list/'+str(replay.thread.id))
    else :
        form = ReplayForm(instance=replay)
        del form.fields['author']
        del form.fields['thread']


    return render(request,'replayform.html',{'form':form})



def delReplay(request,id):
    try:
        replay = Replay.objects.get(pk=id)
        replay.delete()

    except Replay.DoesNotExist:
        return HttpResponse('Not found')

    return redirect('/replay')
