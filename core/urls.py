from django.urls import path
from .views import ViewSetUserChanges, NewUser

urlpatterns = [
    path('users/', ViewSetUserChanges.as_view(), name='get_users'),
    path('newuser/<pk>/', NewUser.as_view(), name='new-user')
]
