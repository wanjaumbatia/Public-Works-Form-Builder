from django.urls import path

from forms.views import  forms_list, submit_form, submissions_list, test_pdf

urlpatterns = [
     path("", forms_list, name="forms-list"),
     path("submission/<str:pk>", submit_form, name="submit-form"),
     path("submissions/<str:pk>", submissions_list, name="form-submissions"),
     path("test/<str:pk>", test_pdf, name="pdf_test"),
]
