from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_superuser': {'write_only': True}
        }
        read_only_fields = ('id',)

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        is_superuser = validated_data['is_superuser']
        user_obj = User.objects.create(username=username, email=email)
        user_obj.set_password(password)
        basic_permissions = Group.objects.get(name="Basic Permissions")
        if is_superuser:
            permissions = Group.objects.get(name="Admin")
        else:
            permissions = Group.objects.get(name="Read Only")
        user_obj.groups.add(basic_permissions)
        user_obj.groups.add(permissions)
        user_obj.is_superuser = is_superuser
        user_obj.save()
        return validated_data
