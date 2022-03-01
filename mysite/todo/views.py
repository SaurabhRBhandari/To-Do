from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from django.contrib.auth.models import User
from django.views.generic import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class TaskListView(ListView):
    model = Task
    template_name = 'todo/home.html'
    context_object_name = 'tasks'
    ordering = ['-timestamp']
    paginate_by = 5


class UserTaskListView(ListView):
    model = Task
    template_name = 'todo/user_task.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Task.objects.filter(user=user).order_by('-timestamp')


class TaskDetailView(DetailView):
    model = Task

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    q = get_object_or_404(Task, pk=self.kwargs.get('pk'))
    #    return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task', 'description', 'task_image','deadline']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['task', 'description','deadline']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = "/"

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False