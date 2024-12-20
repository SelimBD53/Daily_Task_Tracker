from django.urls import path
from To_Do.views import store_tasks, show_task, is_completed, delete_task, task_completed

urlpatterns = [
    path('', store_tasks, name='store_task'),
    path('show_task/', show_task, name='show_task'),
    path('is_copmletaed/<int:id>', is_completed, name='iscompleated'),
    path('task_completed/', task_completed, name='taskcomplete'),
    path('delete_task/<int:id>', delete_task, name='deletetask'),
]