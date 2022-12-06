from django.urls import path
from . import views

urlpatterns = [
    path("group/", views.GroupAssets.as_view()),
    path("group/", views.GroupDetails.as_view()),
]
