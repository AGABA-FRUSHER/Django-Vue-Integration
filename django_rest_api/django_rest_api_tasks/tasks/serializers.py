from rest_framework import serializers, routers, viewsets
from .models import Tasks


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'completed', 'created_at')