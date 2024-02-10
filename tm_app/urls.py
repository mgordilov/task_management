from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('departments/', views.DepartmentList.as_view(), name='department_view'),
    path('department/create', views.DepartmentCreate.as_view(), name='department_create'),
    path('department/<int:pk>/update', views.DepartmentUpdate.as_view(), name='department_update'),
    path('department/<int:pk>/delete', views.DepartmentDelete.as_view(), name='department_delete'),

    path('staff/', views.staff, name='staff'),

    path('tasks/', views.TaskList.as_view(), name='task_view'),
    path('task/create', views.TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete', views.TaskDelete.as_view(), name='task_delete'),
    path('task/<int:pk>', views.task_detail, name='task_detail'),
    path('task/<int:pk>/assign', views.assign_task, name='assign_task'),
    path('task/<int:pk>/unassign', views.unassign_task, name='unassign_task'),
    path('task/<int:pk>/complete', views.markAsCompleted, name='markAsCompleted'),

]