from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.helper import *

from cat_forum.models import *
# from thread import *

def index_action(request):
    cats = Category.objects.all()
    return render(request,'index.html',{'cats':cats,'user1':get_user(request)})