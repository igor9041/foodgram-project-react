from rest_framework import permissions
from djoser import views

from .models import CustomUser
from .serializers import CustomUserSerializer
from .pagination import LimitPageNumberPagination


class UserViewSet(views.UserViewSet):
    serializer_class = CustomUserSerializer
    pagination_class = LimitPageNumberPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return CustomUser.objects.all()