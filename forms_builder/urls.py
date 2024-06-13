from django.urls import path
from forms_builder.views import (create_section, delete_field, delete_section, FormCreateView,
    FormDeleteView, FormDetailView, FormListView, FormUpdateView, delete_section, create_field)

urlpatterns = [
    path("forms-builder/", FormListView.as_view(), name="forms-builder-list"),
    path("forms-builder/create", FormCreateView.as_view(), name="forms-builder-create"),
    path("forms-builder/edit/<str:pk>", FormUpdateView.as_view(), name="forms-builder-edit"),
    path("forms-builder/details/<str:pk>", FormDetailView.as_view(), name="forms-builder-details"),    
    path("forms-builder/delete/<str:pk>", FormDeleteView.as_view(), name="forms-builder-delete"),

    path("forms-builder/create-section/<str:pk>", create_section, name="forms-builder-create-section"),
    path("forms-builder/delete-section/<str:pk>", delete_section, name="forms-builder-delete-section"),
    path("forms-builder/create-field/<str:pk>", create_field, name="forms-builder-create-field"),
    path("forms-builder/delete-field/<str:pk>", delete_field, name="forms-builder-delete-field"),
]
