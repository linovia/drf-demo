from django.contrib.auth import get_user_model
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = models.Task

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        username = owner_data.pop('username')
        owner = get_user_model().objects.get_or_create(username=username)[0]
        task = models.Task.objects.create(owner=owner, **validated_data)
        return task

    def update(self, instance, validated_data):
        owner_data = validated_data.pop('owner')
        username = owner_data.pop('username')
        owner = get_user_model().objects.get_or_create(username=username)[0]
        instance.owner = owner
        instance.name = validated_data['name']
        return instance
