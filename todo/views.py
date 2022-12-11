from django.shortcuts import render

# Create your views here.
from .models import Todo
from rest_framework import viewsets,permissions,generics
from .serializers import TodoSeriarizer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSeriarizer
    permission_classes = (permissions.IsAuthenticated,)