from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','owner', 'title', 'description', 'completed', 'created_at']
        read_only_fields = ['created_at', 'owner']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate(self, data):
        completed = data.get('completed', getattr(self.instance, 'completed', False))
        description = data.get('description', getattr(self.instance, 'description', ''))
    
        if completed and not description:
            raise serializers.ValidationError("Completed tasks must have a description.")
        return data