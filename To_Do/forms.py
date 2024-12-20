from django import forms
from To_Do.models import TaskModel

class TaskModelForm(forms.ModelForm):
    # Due_Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
     
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
       