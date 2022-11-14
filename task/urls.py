from django.urls import path

from task.views import index, TaskCreateView, TagCreateView, TaskUpdateView, TagUpdateView, TaskDeleteView, \
    TagDeleteView, TaskListView, TagListView, change_status

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/change/<int:pk>/", change_status, name="task-change")
]


app_name = "task"