from django.urls import path
from . import views

urlpatterns = [
    path("pet", views.PetAssets.as_view()),
    path("pet/<pet_id>", views.PetDetails.as_view()),
]
