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
        "created_at",
        "active",
    ]
    list_filter = ["name", "active", "category", "brand"]
    list_editable = ["active", "price", "stock"]
    search_fields = ["name", "description", "brand"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    list_filter = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    list_filter = ["name", "created_at"]
    search_fields = ["name"]
