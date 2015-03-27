from user.helper import *

from django.shortcuts import render,redirect


def login_required(function):
  def wrap(request, *args, **kwargs):

        user = get_user(request)
        if user:
             return function(request, *args, **kwargs)
        else:
            return render(request,'error.html',{'msg': 'You Must Be Logged In'})

  wrap.__doc__=function.__doc__
  wrap.__name__=function.__name__
  return wrap


def admmin_required(function):
  def wrap(request, *args, **kwargs):
        user = get_user(request)
        if user and user.role == 'a':
             return function(request, *args, **kwargs)
        else:
            return render(request,'error.html',{'msg': 'You Must Be Admin'})

  wrap.__doc__=function.__doc__
  wrap.__name__=function.__name__
  return wrap

def same_user_required(function):
  def wrap(request, *args, **kwargs):
        user = get_user(request)
        if user and user.id == kwargs['id']:
             return function(request, *args, **kwargs)
        else:
            return render(request,'error.html',{'msg': 'You Must Be The Same User'})

  wrap.__doc__=function.__doc__
  wrap.__name__=function.__name__
  return wrap

def same_user_or_admin_required(function):
  def wrap(request, *args, **kwargs):
        user = get_user(request)
        if user and user.id == kwargs['id'] or user.role == 'a':
             return function(request, *args, **kwargs)
        else:
            return render(request,'error.html',{'msg': 'You Must Be The Same User Or The Admin'})

  wrap.__doc__=function.__doc__
  wrap.__name__=function.__name__
  return wrap

def anonymous_required(function):
  def wrap(request, *args, **kwargs):
        user = get_user(request)
        if not user :
             return function(request, *args, **kwargs)
        else:
            return render(request,'error.html',{'msg': 'You Must Logout First'})

  wrap.__doc__=function.__doc__
  wrap.__name__=function.__name__
  return wrap