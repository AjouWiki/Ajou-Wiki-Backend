from django.urls import path

from . import views

urlpatterns = [
    path("create", views.CreateTag.as_view()),
    path("delete", views.DeleteTag.as_view()),
    path("get", views.GetTagList.as_view()),
]