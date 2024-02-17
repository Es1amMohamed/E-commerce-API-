from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "price",
        "stock",
        "category",
        "brand",
        "rating",
        "created_at",
        "active",
    ]
    list_filter = ["name", "active", "category", "brand"]
    list_editable = ["active", "price", "stock"]
    search_fields = ["name", "description", "brand"]
    prepopulated_fields = {"slug": ("name",)}
