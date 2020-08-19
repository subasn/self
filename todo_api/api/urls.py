from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiOverview,name="api-overview"),
    path('task_list/',views.taskList,name="taskList"),
    path('task_detail/<str:pk>/',views.taskDetail,name="taskDetail"),
    path('create_task/',views.taskCreate,name="createTask"),
    path('update_task/<str:pk>/',views.updateTask,name="updateTask"),
    path('delete_task/<str:pk>/',views.taskDelete,name="taskDelete "),
]