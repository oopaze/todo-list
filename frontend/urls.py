from django.urls import path

from .views import todo_list

app_name = 'frontend'

urlpatterns = [
    path('', todo_list, name='todo-list'),
]
