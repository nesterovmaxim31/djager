from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("problems/", views.problems, name="problems"),
    path("problems2/", views.problems2, name="problems2"),
    path("<slug:slug>/", views.D.as_view(), name="iter_2")    
]