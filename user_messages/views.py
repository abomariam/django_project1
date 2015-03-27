from django.shortcuts import render
from django.shortcuts import redirect
from user_messages.models import *
from user.models import *
from user.helper import *
from user.decorators import *
from django.db.models import Q
from copy import deepcopy
from user.forms import *
# Create your views here.


@login_required
def messages_get(request, id):
    user = get_user(request)
    try:
        other_user = User.objects.get(pk=id)
    except:
        render(request,'error.html',{'msg':"Wrong User"})

    if request.method == 'POST':
        data = deepcopy(request.POST)
        data['sender'] = other_user.id
        data['reciever'] = user.id

        form = MessageForm(data)
        if form.is_valid():
            form.save()


    form = MessageForm()
    del form.fields['sender']
    del form.fields['reciever']
    form.fields['body'].label = ''

    messages = Messages.objects.filter(Q(sender=user.id , reciever = id) | Q(sender=id , reciever = user.id)  ).order_by('time')

    user_form = MessageForm()
    user_form.fields['sender'].label = "Choose User"
    del user_form.fields['body']
    del user_form.fields['reciever']

    return render(request, 'list.html', {'messages': messages, 'user1': user,'other_user': other_user , 'form':form,'user_form':user_form})

@login_required
def messages_index(request):
    user = get_user(request)
    users = User.objects.all()
    return render(request, 'messages_index.html', {'user1': user,'users':users})