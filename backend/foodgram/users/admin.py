from django.contrib.admin import ModelAdmin, register

from foodgram.settings import EMPTY_STRING_FOR_ADMIN_PY

from .models import CustomUser, Follow

ModelAdmin.empty_value_display = EMPTY_STRING_FOR_ADMIN_PY


@register(CustomUser)
class MyUserAdmin(ModelAdmin):
    list_display = (
        'id', 'username', 'email',
        'first_name', 'last_name',)
    search_fields = ('username', 'email')


@register(Follow)
class SubscriptionAdmin(ModelAdmin):
    list_display = ('user', 'author',)
    list_filter = ('user', 'author',)
