from django.contrib import admin
from django.urls import path
from .views import (task_create, task_detail, task_delete, task_list, task_update, task_views)

urlpatterns = [
    path('', task_views, name='views'),
    path('list', task_list, name='list'),
    path('create', task_create, name='create'),
    path('detail/<str:slug>', task_detail, name='detail'),
    path('update/<str:slug>', task_update, name='update'),
    path('delete/<str:slug>', task_delete, name='delete'),
]
