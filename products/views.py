from django.shortcuts import render
from .models import *
from .serializers import ProductsSerializer
from rest_framework import viewsets

# Create your views here.


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
