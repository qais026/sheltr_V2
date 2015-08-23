from django.contrib import admin
from .models import Post, Category, Provider
from django.db import models
from django.forms import CheckboxSelectMultiple

class ProviderAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Provider)
