from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from projects.models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework.exceptions import PermissionDenied
from rest_framework import status

from users.models import User
from .serializers import UserSerializer

class DashboardView(APIView):
    def get(self, request):
        user = request.user

        tasks = Task.objects.filter(assigned_to=user)

        data = {
            "total": tasks.count(),
            "completed": tasks.filter(status='done').count(),
            "in_progress": tasks.filter(status='in_progress').count(),
            "overdue": tasks.filter(due_date__lt=now(), status__in=['todo', 'in_progress']).count(),
        }

        return Response(data)

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()  
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data = request.data,
            context = {
                "user": request.user
            }
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        if not project_id:
            return Task.objects.none()
        return Task.objects.filter(project_id = project_id)

    def create(self, request, *args, **kwargs):
        project_id = kwargs.get("project_id")
        serializer = TaskSerializer(
            data=request.data,
            context = {
                "project_id":project_id,
                "user":request.user
            }
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        assigned_to = request.data.get("assigned_to")
        print(assigned_to)

        if assigned_to is not None:
            instance.assigned_to_id = assigned_to
            instance.save(update_fields=["assigned_to"])

        return Response(self.get_serializer(instance).data)


class TaskList(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to = self.request.user)