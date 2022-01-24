from django.shortcuts import render

# Create your views here.
from djoser import views

from users.models import CustomUser



class UserViewSet(views.UserViewSet):

    def get_queryset(self):
        return CustomUser.objects.all()