from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('chatrooms/', ChatRoomListCreateAPIView.as_view()),
    path('messages/', MessageListCreateAPIView.as_view()),
]