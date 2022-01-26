from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import TagSerializer
from .models import Tag


class BaseViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    permission_classes = (AllowAny,)


class TagViewSet(BaseViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
