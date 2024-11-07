from django.urls import path
from . import views
from .views import TaskListAPIView

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('todos/', TaskListAPIView.as_view(), name='task_list_api')
]
