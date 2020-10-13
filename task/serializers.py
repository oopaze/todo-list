from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Task
        exclude = ('id', 'criado_em', 'atualizado_em')
