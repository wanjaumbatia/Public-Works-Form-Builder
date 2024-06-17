from django.urls import path

from forms.views import  forms_list, submit_form, submissions_list

urlpatterns = [
     path("", forms_list, name="forms-list"),
     path("submission/<str:pk>", submit_form, name="submit-form"),
     path("submissions/<str:pk>", submissions_list, name="form-submissions"),
]
