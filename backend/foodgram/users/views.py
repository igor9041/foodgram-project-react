from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from djoser.views import UserViewSet

from .pagination import Paginator
from .serializers import CustomUserSerializer

User = get_user_model()


class UserViewSet(UserViewSet):
    pagination_class = Paginator
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, permission_classes=[AllowAny])
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
