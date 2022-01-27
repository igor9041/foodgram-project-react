from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Tag, Ingredient

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {'color': {'required': True}}
        

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
