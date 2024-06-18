from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from users.forms import UserForm

class UsersListView(ListView):
    model = User
    context_object_name = 'users'
    template_name='users/list.html'
    permissions = []

class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name='users/details.html'   

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "users/create.html"
    success_url = reverse_lazy('users-list')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/edit.html"
    success_url = reverse_lazy('users-list')

class UserDeleteView(DeleteView):
    model = User
    context_object_name = 'user'
    template_name = "users/delete.html"
    success_url = reverse_lazy('users-list')
    

# TODO: Send Email to user upon user save