from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),

    path('profile/<str:user_id>', views.user_profile, name='user-profile'),

    path('room/<str:room_id>', views.room, name='room'),
    path('create-room', views.create_room, name='create-room'),
    path('update-room/<str:room_id>', views.update_room, name='update-room'),
    path('delete-room/<str:room_id>', views.delete_room, name='delete-room'),
    path('delete-message/<str:message_id>', views.delete_message, name='delete-message'),
    path('update-user', views.update_user, name='update-user'),
]