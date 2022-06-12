from django.shortcuts import render
from .models import *
from message.models import *
from django.contrib.auth import get_user_model
from chat.models import ChatRoom
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

def index(request):
    # users = get_user_model().objects.all()
    # filtered_users = []
    # for user in users:
    #     for chatroom in request.user.chatrooms.all():
    #         if user in [chatroom.user1, chatroom.user2]:
    #             print(user.username)
    #         else:
    #             filtered_users.append(user)
    # return render(request, 'index.html', context={'users': filtered_users})
    try:
        users = get_user_model().objects.all()
        chatted_users = []
        filtered_users = []
        for i in request.user.chatrooms.all():
            chatted_users.append(i.user1)
            chatted_users.append(i.user2)
        for user in users:
            if user in chatted_users:
                pass
            else:
                filtered_users.append(user)

        return render(request, 'index.html', context={'users': filtered_users})
    except:
        return render(request, 'index.html')
  

def getMessages(request, chatroom_user2_username):
    user2 = get_user_model().objects.get(username=chatroom_user2_username)
    print(user2.username)
    print(f"xxxxxxxxxxxxxxxxxx - {user2.username} ")
    try:
    
        # chatroom = ChatRoom.objects.get(user1=request.user, user2=user2)
        chatroom = get_object_or_404(ChatRoom, user1=request.user, user2=user2)

    except:
    
        # chatroom = ChatRoom.objects.get(user1=user2, user2=request.user)
        chatroom = get_object_or_404(ChatRoom, user1=user2, user2=request.user)
    messages = chatroom.messages.all()
    return JsonResponse({'messages': list(messages.values()), 'author_id': request.user.id})

def addMessage(request, chatroom_user2_username):
    if request.method == 'POST':
        text = request.POST['text']
        print(text)
        author = request.user
        user2 = get_user_model().objects.get(username=chatroom_user2_username)
        try:
            chatroom = ChatRoom.objects.get(user1=request.user, user2=user2)
        except:
            try:
                chatroom = ChatRoom.objects.get(user1=user2, user2=request.user)
            except:
                chatroom = ChatRoom.objects.create(user1=request.user, user2=user2)
                chatroom.save()
        print(chatroom.user1.username, chatroom.user2.username)
        new_message = Message.objects.create(text=text, chatroom=chatroom, author=author)
        new_message.save()
        chatroom.messages.add(new_message)
        chatroom.save()
        
        if chatroom in request.user.chatrooms.all():
            pass
        else:
            request.user.chatrooms.add(chatroom)
            request.user.save()
        
        if chatroom in user2.chatrooms.all():
            pass
        else:
            user2.chatrooms.add(chatroom)
            user2.save()
        return HttpResponse('success !')