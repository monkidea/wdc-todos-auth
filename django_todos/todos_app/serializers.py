from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'owner', 'title', 'completed')

    owner = serializers.ReadOnlyField(source='owner.username')



class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
