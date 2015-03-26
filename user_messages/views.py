from django.shortcuts import render
from django.shortcuts import redirect
from user_messages.models import *
from user.models import *

# Create your views here.


def messages_list(request,sender_id):
    msg_sender = User.objects.get(pk=sender_id)
    msg_reciever = User.objects.get(pk=2)
    message = messages.objects.filter(sender=msg_sender,reciever = msg_reciever)
    return render(request, 'list.html', {'messages': message})

def messages_add(request,sender_id):
    if request.method=='GET':
        message_form=MessageForm()
        return render(request,'add_message.html',{'message_form':message_form})
    elif request.method=='POST':
         msg_sender = User.objects.get(pk=sender_id)
         msg_reciever = User.objects.get(pk=2)
         message = messages.objects.filter(sender=msg_sender,reciever = msg_reciever)
         message_form=MessageForm(request.POST)
         if message_form.is_valid():
             message_form.save()
             return redirect('/messages/'+sender_id)

         else:
             return render(request,'add_message.html',{'message_form':message_form})
