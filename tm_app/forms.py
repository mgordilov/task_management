from django import forms
from .models import User, Department, Task
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'department', 'managed_by', 'due_date']
    
    def __init__(self, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        self.fields['managed_by'].queryset = User.objects.filter(userprofile__is_manager=True)

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'department', 'managed_by', 'due_date', 'is_completed']

