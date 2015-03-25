from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import *
from user.models import *
from django.core import serializers
# Create your views here.

def add_user(request):

    if request.method == 'POST' :
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
    else :
        form = UserForm()
    user = User.objects.get(pk=1)
    obj = serializers.serialize('json', [ user, ])
    user2 = serializers.deserialize('json',obj)
    arr = []
    for u in user2:
        arr.append(u)
    request.session['test'] = obj
    return render(request,'user_form.html',{'form':form, 'user':request.user,'obj':arr[0].object.email})


def edit_user(request,id):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse("User Not Found")

    if request.method == 'POST' :
        form = UserForm(data=request.POST,instance=user)
        del form.fields['password']
        if form.is_valid():
            form.save()
            return redirect('/user')
        else:
            form.fields['email'].widget.attrs['readonly'] = True
    else :
        form = UserForm(instance=user)
        form.fields['email'].widget.attrs['readonly'] = True
        del form.fields['password']


    return render(request,'user_form.html',{'form':form})

def list_users(request):
    try:
        users = User.objects.all()
    except:
        users = []

    return render(request,'index.html',{'users':users})


def delete_user(request,id):
    try:
        user = User.objects.get(pk=id)
        user.delete()
        return redirect('/user')
    except:
        return HttpResponse("User Not Found")
