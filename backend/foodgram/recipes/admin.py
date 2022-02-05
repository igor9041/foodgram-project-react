from django.contrib.admin import ModelAdmin, register

from foodgram.settings import EMPTY_STRING_FOR_ADMIN_PY

from recipes.models import (Favorite, Ingredient, IngredientAmount, Recipe,
                            ShoppingCart, Tag)


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ('author', 'name', 'favorited')
    search_fields = ('author', 'name',)
    list_filter = ('name', 'author', 'tags')
    
    def favorited(self, obj):
        return Favorite.objects.filter(recipe=obj).count()


@register(Ingredient)
class RecipeAdmin(ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('author', 'name',)
    list_filter = ('name',)