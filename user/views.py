from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import *
from user.models import *
from user.helper import *
# Create your views here.

def logout_user(request):
    try:
        del request.session['user1']
    except:
        pass
    return redirect('/')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=request.POST.get('email'), password = request.POST.get('password'))
                save_user(request,user)

                return redirect('/')
            except:
                return render(request,'login.html',{'form': form, 'error_msg':"Invalid Email or Password"})
    form = LoginForm()
    return render(request,'login.html',{'form': form})

def add_user(request):
    if request.method == 'POST' :
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
    else :
        form = UserForm()

    return render(request,'user_form.html',{'form':form, 'user':get_user(request),'user1':get_user(request)})


def register_user(request):
    if request.method == 'POST' :
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
    else :
        form = UserForm()
        form.fields['is_banned'].widget = forms.HiddenInput()
        form.fields['role'].widget = forms.HiddenInput()

    return render(request,'user_form.html',{'form':form, 'user':get_user(request),'user1':get_user(request)})

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


    return render(request,'user_form.html',{'form':form, 'user1':get_user(request)})

def list_users(request):
    try:
        users = User.objects.all()
    except:
        users = []

    return render(request,'user_list.html',{'users':users, 'user1':get_user(request)})


def delete_user(request,id):
    user = get_user(request)
    if user and user.role == 'a':
        try:
            user = User.objects.get(pk=id)
            user.delete()
            return redirect('/user')
        except:
            return HttpResponse("User Not Found")
    else:
        return HttpResponse("You Are Not Authorized")

