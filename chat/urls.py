from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('getMessages/<str:chatroom_user2_username>', getMessages, name='getMessages'),
    path('addMessage/<str:chatroom_user2_username>', addMessage, name='addMessage')
]