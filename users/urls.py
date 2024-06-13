from django.urls import path
import django.views.generic
from users.views import UserCreateView, UserDeleteView, UserDetailView, UsersListView, UserUpdateView

urlpatterns = [
    path("", UsersListView.as_view(), name="users-list"),
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("details/<str:pk>", UserDetailView.as_view(), name="user-details"),
    path("edit/<str:pk>", UserUpdateView.as_view(), name="user-update"),
    path("delete/<str:pk>", UserDeleteView.as_view(), name="user-delete"),
    
]
