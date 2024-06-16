from django.urls import path

from forms.views import  forms_list, submit_form

urlpatterns = [
     path("", forms_list, name="forms-list"),
     path("/submission/<str:pk>", submit_form, name="submit-form"),
]
