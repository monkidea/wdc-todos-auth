from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication

from .serializers import TodoSerializer
from .models import Todo


class IsTodoOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class TodoViewSet(viewsets.ModelViewSet):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    authentication_classes = (
        authentication.TokenAuthentication,
        # authentication.BasicAuthentication,
    )
    permission_classes = (
        # permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAuthenticated,
        IsTodoOwner,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
