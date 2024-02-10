from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from . import forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def home(request):
    department_list = models.Department.objects.all()
    return render(request, 'tm_app/home.html', {'department_list': department_list})

class DepartmentCreate(CreateView):
    model = models.Department
    form_class = forms.DepartmentCreateForm
    template_name = 'tm_app/department_create.html'

class DepartmentList(ListView):
    model = models.Department
    template_name = 'tm_app/department_view.html'

class DepartmentUpdate(UpdateView):
    model = models.Department
    form_class = forms.DepartmentUpdateForm
    template_name = 'tm_app/department_update.html'

class DepartmentDelete(DeleteView):
    model = models.Department
    success_url = '/departments/'
    template_name = 'tm_app/department_delete.html'

def staff(request):
    users = User.objects.all()
    departments = models.Department.objects.all()
    return render(request, 'tm_app/staff.html', {'users': users, 'departments': departments})

class TaskList(LoginRequiredMixin, ListView):
    model = models.Task
    template_name = 'tm_app/task_view.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = models.Task
    form_class = forms.TaskCreateForm
    template_name = 'tm_app/task_create.html'

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = models.Task
    form_class = forms.TaskUpdateForm
    template_name = 'tm_app/task_update.html'

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = models.Task
    success_url = '/tasks/'
    template_name = 'tm_app/task_delete.html'


@login_required
def task_detail(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    return render(request, 'tm_app/task_detail.html', {'task': task})

@login_required
def assign_task(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    task.assigned_to.add(request.user)
    task.save()
    return redirect('task_detail', pk=pk)

@login_required
def unassign_task(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    task.assigned_to.remove(request.user)
    task.save()
    return redirect('task_detail', pk=pk)

@login_required
def markAsCompleted(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(models.Task, pk=pk)
        task.is_completed = True
        task.save()
        return redirect('task_detail', pk=pk)
    task = get_object_or_404(models.Task, pk=pk)
    return render(request, 'tm_app/task_complete.html', {'task': task})

