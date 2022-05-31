from django.contrib import admin
from .models import CustomUser, UserInfo


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'password',
    )

    
class UserInfoAdmin(admin.ModelAdmin):
    list_display = (
        'get_user',
        'avatar',
        'address',
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
