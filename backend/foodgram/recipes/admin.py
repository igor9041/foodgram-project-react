from django.contrib import admin
from .models import (Favorites, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Tag)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color',)
    search_fields = ('name', 'color',)
    list_filter = ('color',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement',)
    search_fields = ('name', 'measurement',)
    list_filter = ('measurement',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('author', 'tags','name')


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
