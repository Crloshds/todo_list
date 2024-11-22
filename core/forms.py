from django import forms
from django.forms import ModelForm

from .models import Task

class TaskForm(forms.ModelForm):

    title = forms.CharField(label = 'Título',widget=forms.TextInput(attrs={'placeholder':'Título da tarefa', 'style': 'width: 27.5rem;'}))

    class Meta:
        model = Task
        fields = "__all__"