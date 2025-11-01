from django.shortcuts import render
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework import viewsets,permissions

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = []

    # def get_queryset(self):
    #     return Task.objects.filter(user=self.request.user)
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
