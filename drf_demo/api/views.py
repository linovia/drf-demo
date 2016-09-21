from rest_framework import viewsets
from . import models
from . import serializers


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
