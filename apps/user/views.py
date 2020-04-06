from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer

User = get_user_model()


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.pk,
            'token': token.key,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'is_active': user.is_active
        })


class UserViewSet(viewsets.ModelViewSet):
    """docstring for UserViewSet"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = User.objects.all()

        return queryset
