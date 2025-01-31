from django.urls import path
from . import views

urlpatterns = [
    path("",view=views.taskList,name="tasks")
]