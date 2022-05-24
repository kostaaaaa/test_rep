from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'pub_date',
        'image',
        'username',
    )
    readonly_fields = (['username'])


admin.site.register(Post, PostAdmin)