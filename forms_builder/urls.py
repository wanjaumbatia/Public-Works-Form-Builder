from django.urls import path
from forms_builder.views import (create_choice, create_field, create_section, delete_choice,
    delete_field, delete_section, delete_section, FormCreateView, FormDeleteView, FormDetailView,
    FormListView, FormUpdateView, preview, publish, pulldown)

urlpatterns = [
    path("", FormListView.as_view(), name="forms-builder-list"),
    path("create", FormCreateView.as_view(), name="forms-builder-create"),
    path("publish/<str:pk>", publish, name="forms-builder-publish"),
    path("pulldown/<str:pk>", pulldown, name="forms-builder-pulldown"),
    path("edit/<str:pk>", FormUpdateView.as_view(), name="forms-builder-edit"),
    path("details/<str:pk>", FormDetailView.as_view(), name="forms-builder-details"),    
    path("delete/<str:pk>", FormDeleteView.as_view(), name="forms-builder-delete"),

    path("create-section/<str:pk>", create_section, name="forms-builder-create-section"),
    path("delete-section/<str:pk>", delete_section, name="forms-builder-delete-section"),
    path("create-field/", create_field, name="forms-builder-create-field"),
    path("delete-field/<str:pk>", delete_field, name="forms-builder-delete-field"),
    path("create-choice/", create_choice, name="forms-builder-create-choice"),
    path("delete-choice/<str:pk>", delete_choice, name="forms-builder-delete-choice"),
    
    path("preview/<str:pk>", preview, name="forms-builder-preview"),
]
