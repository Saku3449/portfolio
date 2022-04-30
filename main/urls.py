from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("base/", views.BaseView.as_view(), name="base"),
    path("bio/", views.BioView.as_view(), name="bio"),
    path("blog/<int:pk>", views.BlogView.as_view(), name="blog"),
]
