from rest_framework import serializers
from projects.models import Project, Task
from users.models import User
from users.api.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.id')

    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        user = self.context.get("user")

        return Project.objects.create(
            created_by=user,
            **validated_data
        )
    
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["project", "created_by"]

    def create(self, validated_data):
        project_id = self.context.get("project_id")
        user = self.context.get("user")

        return Task.objects.create(
            project_id=project_id,
            created_by=user,
            **validated_data
        )
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.save()
        return instance
    
