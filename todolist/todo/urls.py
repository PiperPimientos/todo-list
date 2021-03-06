from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:todo_id>/", views.detail, name="index"),
    path("<int:todo_id>/results", views.results, name="index"),
]