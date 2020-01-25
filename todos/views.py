from rest_framework import viewsets

from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    search_fields = [
        'title',
    ]
    filterset_fields = [
        'is_publish',
        'is_complete',
    ]

