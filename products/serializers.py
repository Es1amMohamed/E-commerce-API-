from .models import *
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ["slug"]
