from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('create/', views.create_task, name='create_task'),
    path('end_task:<int:id>/', views.end_task, name='end_task'),
]