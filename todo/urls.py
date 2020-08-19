from django.urls import path
from . import views

urlpatterns=[
    path('',views.todo,name="todo"),
    path('updateTask/<str:pk>/',views.updateTask,name="updateTask"),
    path('deleteTask/<str:pk>/',views.deleteTask,name="deleteTask")
]