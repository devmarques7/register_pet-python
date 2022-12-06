from django.urls import path
from . import views

urlpatterns = [
    path("trait/", views.TraitAssets.as_view()),
    path("trait/", views.TraitDetails.as_view()),
]
