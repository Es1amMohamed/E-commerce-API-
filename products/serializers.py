from .models import *
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        exclude = ["slug"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        


