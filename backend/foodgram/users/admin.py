from django.contrib import admin
from users.models import CustomUser, Subscribe


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
    )
    list_filter = ('email', 'username')


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'author',
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subscribe, SubscribeAdmin)