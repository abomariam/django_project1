from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import *
from user.models import *
from user.helper import *
from copy import deepcopy
from user.decorators import *
# Create your views here.

@login_required
def logout_user(request):
    try:
        del request.session['user1']
    except:
        pass
    return redirect('/')

@anonymous_required
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=request.POST.get('email'), password = request.POST.get('password'))
                if user.is_banned:
                    return render(request,'error.html',{'msg':'Your Account is Locked, Please Contact your administrator'})
                save_user(request,user)

                return redirect('/')
            except:
                return render(request,'login.html',{'form': form, 'error_msg':"Invalid Email or Password"})
    form = LoginForm()
    return render(request,'login.html',{'form': form})

@admmin_required
def add_user(request):
    if request.method == 'POST' :
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
    else :
        form = UserForm()

    return render(request,'user_form.html',{'form':form, 'user':get_user(request),'user1':get_user(request)})

@anonymous_required
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

@same_user_or_admin_required
def edit_user(request,id):
    loggedin_user = get_user(request)
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse("User Not Found")

    if request.method == 'POST' :
        data = deepcopy(request.POST)
        data['password'] = user.password
        if loggedin_user.role != 'a':
            data['is_banned'] = user.is_banned
            data['role'] = user.role
        form = UserForm(data=data,instance=user)
        del form.fields['password']
        if form.is_valid():
            form.save()
            return redirect('/user/profile/'+str(id))
        else:
            form.fields['email'].widget.attrs['readonly'] = True
    else :
        form = UserForm(instance=user)
        form.fields['email'].widget.attrs['readonly'] = True
        del form.fields['password']
        if loggedin_user.role != 'a':
            del form.fields['is_banned']
            del form.fields['role']


    return render(request,'user_form.html',{'form':form, 'user1':get_user(request)})

@admmin_required
def list_users(request):
    try:
        users = User.objects.all()
    except:
        users = []

    return render(request,'user_list.html',{'users':users, 'user1':get_user(request)})

@admmin_required
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

@same_user_or_admin_required
def profile_user(request,id):
    user = User.objects.get(pk=id)

    if user :
        return render(request,'profile.html',{'user1':user})
    else:
        return HttpResponse("You Are not logged in")