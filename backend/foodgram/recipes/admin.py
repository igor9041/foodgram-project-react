from django.contrib.admin import ModelAdmin, register

from foodgram.settings import EMPTY_STRING_FOR_ADMIN_PY

from recipes.models import (Favorite, Ingredient, IngredientAmount, Recipe,
                            ShoppingCart, Tag)

ModelAdmin.empty_value_display = EMPTY_STRING_FOR_ADMIN_PY


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'author',
        'name',
        'favorited'
    )
    search_fields = ('author', 'name',)
    list_filter = ('name', 'author', 'tags')
    readonly_fields = ("favorited",)

    def favorited(self, obj):
        return Favorite.objects.filter(recipe=obj).count()

    favorited.short_description = "В избранном"


@register(Ingredient)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'name',
        'measurement_unit'
    )
    search_fields = ('name',)
    list_filter = ('measurement_unit',)


@register(IngredientAmount)
class IngredientAmountAdmin(ModelAdmin):
    list_display = (
        "ingredient",
        "recipe",
        "amount"
    )


@register(ShoppingCart)
class ShoppingCartAdmin(ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        "name",
        "color",
        "slug"
    )
