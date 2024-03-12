from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        "Category", verbose_name="category", on_delete=models.CASCADE
    )
    brand = models.ForeignKey("Brand", verbose_name="brand", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Products"
        verbose_name = "product"

    def __str__(self):
        return self.name
    
    def __save__(self, *args, **kwargs):
        self.slug = slugify(self.name)
        Products().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    def __save__(self, *args, **kwargs):
        self.slug = slugify(self.name)
        Category().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name
    
    def __save__(self, *args, **kwargs):
        self.slug = slugify(self.name)
        Brand().save(*args, **kwargs)

