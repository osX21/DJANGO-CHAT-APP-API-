from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from .serializers import *

class UserListAPIView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class ChatRoomListCreateAPIView(ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class MessageListCreateAPIView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
