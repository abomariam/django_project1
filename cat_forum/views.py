from django.shortcuts import render
from cat_forum.models import Category
from cat_forum.models import ForumForm
from cat_forum.models import Forum
from django.http import HttpResponse
from cat_forum.models import CatForm

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
            return render(request, 'list_category.html', {'categories': categories})
        else:
            category_form = CatForm()
            return render(request, 'add_category.html', {'category_form': category_form})
    else:
        return HttpResponse('ERROR OCCURED while editing')


def cat_delete(request, id):
    categories = Category.objects.all()
    cat_id = Category.objects.get(pk=id)
    cat_id.delete()
    return render(request, 'list_category.html', {'categories': categories})


def cat_edit(request, id):
    if request.method == 'GET':
        category = Category.objects.get(pk=id)
        category_form = CatForm(instance=category)
        return render(request, 'add_category.html', {'category_form': category_form})
    elif request.method == 'POST':
        categories = Category.objects.all()
        category = Category.objects.get(pk=id)
        category_form = CatForm(data=request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return render(request, 'list_category.html', {'categories': categories})
        else:
            category_form = CatForm()
            return render(request, 'add_category.html', {'category_form': category_form})

    else:
        return HttpResponse('ERROR OCCURED while editing')


####################  forum  ##################################

def forum_add(request):
    if request.method == 'GET':
        forum_form = ForumForm()
        return render(request, 'add_forum.html', {'forum_form': forum_form})
    elif request.method == 'POST':
        forums = Forum.objects.all()
        forum_form = ForumForm(request.POST)
        if forum_form.is_valid():
            forum_form.save()
            return render(request, 'list_forum.html', {'forums': forums})
        else:
            forum_form = ForumForm()
            return render(request, 'add_forum.html', {'forum_form': forum_form})
    else:
        return HttpResponse('ERROR OCCURED while editing')


def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'list_forum.html', {'forums': forums})


def forum_delete(request, id):
    forums = Forum.objects.all()
    forum_id = Forum.objects.get(pk=id)
    forum_id.delete()
    return render(request, 'list_forum.html', {'forums': forums})


def forum_edit(request, id):
    if request.method == 'GET':
        forum = Forum.objects.get(pk=id)
        forum_form = ForumForm(instance=forum)
        return render(request, 'add_forum.html', {'forum_form': forum_form})

    elif request.method == 'POST':
        forum = Forum.objects.get(pk=id)
        forums = Forum.objects.all()
        forum_form = ForumForm(data=request.POST, instance=forum)
        if forum_form.is_valid():
            forum_form.save()
            return render(request, 'list_forum.html', {'forums': forums})
        else:
            forum_form = ForumForm()
            return render(request, 'add_forum.html', {'forum_form': forum_form})

    else:
        return HttpResponse('ERROR OCCURED while editing')
