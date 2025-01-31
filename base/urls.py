from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate

urlpatterns = [
    path("",view=TaskList.as_view(),name="tasks"),
    path("task/<int:pk>/",view=TaskDetail.as_view(),name="task"),
    path("task-create/",view=TaskCreate.as_view(),name="task-create"),

]