from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'date_joined',
        'branch',
        'email',
        'first_name',
        'last_name',
        'is_active'
    )
    search_fields = ('username',)
    list_filter = ('branch',)
    list_editable = ('branch',)


admin.site.register(User, UserAdmin)
