from django.shortcuts import render,redirect
from cat_forum.models import Category
from cat_forum.models import ForumForm
from cat_forum.models import Forum
from django.http import HttpResponse
from cat_forum.models import CatForm
from copy import deepcopy
from user.helper import *

##################### category #######################################

def cat_list(request):
    categories = Category.objects.all()
    return render(request, 'list_category.html', {'categories': categories})


def cat_add(request):
    if request.method == 'GET':
        category_form = CatForm()
        return render(request, 'add_category.html', {'category_form': category_form})
    elif request.method == 'POST':
        categories = Category.objects.all()
        category_form = CatForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('/')
        else:
            category_form = CatForm()
            return render(request, 'add_category.html', {'category_form': category_form, 'user1':get_user(request)})
    else:
        return HttpResponse('ERROR OCCURED while editing')


def cat_delete(request, id):
    categories = Category.objects.all()
    cat_id = Category.objects.get(pk=id)
    cat_id.delete()
    return redirect('/',{'user1':get_user(request)})


def cat_edit(request, id):
    if request.method == 'GET':
        category = Category.objects.get(pk=id)
        category_form = CatForm(instance=category)
        return render(request, 'add_category.html', {'category_form': category_form, 'user1':get_user(request)})
    elif request.method == 'POST':
        categories = Category.objects.all()
        category = Category.objects.get(pk=id)
        category_form = CatForm(data=request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect('/',{'user1':get_user(request)})
        else:
            return render(request, 'add_category.html', {'category_form': category_form, 'user1':get_user(request)})

    else:
        return HttpResponse('ERROR OCCURED while editing')


####################  forum  ##################################

def forum_add(request,cat_id):
    try:
        cat = Category.objects.get(pk=cat_id)
    except:
        return HttpResponse("Worng Category")

    if request.method == 'GET':
        forum_form = ForumForm()
        del forum_form.fields['category']
        return render(request, 'add_forum.html', {'forum_form': forum_form, 'user1':get_user(request)})
    elif request.method == 'POST':
        forums = Forum.objects.all()

        data = deepcopy(request.POST)
        data['category'] = cat_id

        forum_form = ForumForm(data)
        if forum_form.is_valid():
            forum_form.save()
            return redirect('/',{'user1':get_user(request)})
        else:
            del forum_form.fields['category']
            return render(request, 'add_forum.html', {'forum_form': forum_form, 'user1':get_user(request)})
    else:
        return HttpResponse('ERROR OCCURED while editing')


def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'list_forum.html', {'forums': forums , 'user1':get_user(request)})

def threads_list(request,id):
    try:
        forum = Forum.objects.get(pk=id)
    except:
        return HttpResponse("Forum Not Found")
    return render(request, 'list_threads.html', {'forum': forum, 'user1':get_user(request)})


def forum_delete(request, id):
    forums = Forum.objects.all()
    forum_id = Forum.objects.get(pk=id)
    forum_id.delete()
    return redirect("/")


def forum_edit(request, id):
    if request.method == 'GET':
        forum = Forum.objects.get(pk=id)
        forum_form = ForumForm(instance=forum)
        return render(request, 'add_forum.html', {'forum_form': forum_form, 'user1':get_user(request)})

    elif request.method == 'POST':
        forum = Forum.objects.get(pk=id)
        forums = Forum.objects.all()
        forum_form = ForumForm(data=request.POST, instance=forum)
        if forum_form.is_valid():
            forum_form.save()
            return redirect('/forum/list/'+str(id))
        else:
            return render(request, 'add_forum.html', {'forum_form': forum_form, 'user1':get_user(request)})

    else:
        return HttpResponse('ERROR OCCURED while editing')
