from django.shortcuts import render
from django.shortcuts import redirect
from user_messages.models import *
from user.models import *
from user.helper import *
from user.decorators import *
from django.db.models import Q
from copy import deepcopy
# Create your views here.


def messages_list(request,sender_id):
    msg_sender = User.objects.get(pk=sender_id)
    msg_reciever = User.objects.get(pk=2)
    message = Messages.objects.filter(sender=msg_sender,reciever = msg_reciever)
    return render(request, 'list.html', {'messages': message})

@login_required
def messages_add(request,sender_id):
    if request.method=='GET':
        message_form=MessageForm()
        return render(request,'add_message.html',{'message_form':message_form})
    elif request.method=='POST':
         msg_sender = User.objects.get(pk=sender_id)
         msg_reciever = User.objects.get(pk=2)
         message = Messages.objects.filter(sender=msg_sender,reciever = msg_reciever)
         message_form=MessageForm(request.POST)
         if message_form.is_valid():
             message_form.save()
             return redirect('/messages/'+sender_id)

         else:
             return render(request,'add_message.html',{'message_form':message_form})

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
            del form.fields['sender']
            del form.fields['reciever']
            form.fields['body'].label = ''

    form = MessageForm()
    del form.fields['sender']
    del form.fields['reciever']
    form.fields['body'].label = ''

    messages = Messages.objects.filter(Q(sender=user.id , reciever = id) | Q(sender=id , reciever = user.id)  ).order_by('time')
    return render(request, 'list.html', {'messages': messages, 'user1': user,'other_user': other_user , 'form':form})

@login_required
def messages_index(request):
    user = get_user(request)
    messages = Messages.objects.filter(Q(sender=user.id) | Q(reciever = user.id)  )
    return render(request, 'messages_index.html', {'messages': messages, 'user1': user})