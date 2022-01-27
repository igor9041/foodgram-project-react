import django_filters as filters
from django.contrib.auth import get_user_model

from .models import Ingredient

User = get_user_model()


class IngredientNameFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)