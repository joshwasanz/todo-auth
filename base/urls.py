from django.urls import path
from .views import TaskList

urlpatterns = [
    path("",view=TaskList.as_view(),name="tasks")
]