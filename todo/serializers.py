from rest_framework import serializers
from .models import Todo


class TodoSeriarizer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'done', 'title', 'created', 'updated']