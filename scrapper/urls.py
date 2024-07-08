from django.urls import path

from scrapper.views import query_data

urlpatterns = [
     path("", query_data, name="query"),
]
