from django.contrib import admin
from .models import Post, Category, Provider

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Provider)
