from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def completed(self, request):
        completed_tasks = Task.objects.filter(owner=request.user, completed=True)
        serializer = TaskSerializer(completed_tasks, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        pending_tasks = Task.objects.filter(owner=request.user, completed=False)
        serializer = TaskSerializer(pending_tasks, many=True)
        return Response(serializer.data)