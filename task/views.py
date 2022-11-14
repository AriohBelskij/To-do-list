from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm
from task.models import Task, Tag


def index(request):
    num_task = Task.objects.count()
    num_cars = Tag.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_task": num_task,
        "num_tag": num_cars,
        "num_visits": num_visits + 1,
    }
    return render(request, "task/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    queryset = Task.objects.all()


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "task/tag_list.html"
    queryset = Tag.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("task:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "task/tag_form.html"
    success_url = "/"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "task/tag_confirm_delete.html"


def change_status(request, pk):
    task = Task.objects.get(pk=pk)
    if task.done:
        task.done = False
        task.save()
    else:
        task.done = True
        task.save()
    return HttpResponseRedirect(reverse_lazy("task:task-list"))
