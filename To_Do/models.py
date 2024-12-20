from django.db import models

# Create your models here.

class TaskModel(models.Model):
    
    prirority_choise = [(i, f'{i}') for i in range(9)]

    id = models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.CharField(max_length=100)
    # prirority = models.IntegerField(choices=prirority_choise)
    # Due_Date = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)