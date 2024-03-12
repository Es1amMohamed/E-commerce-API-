from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CustomPagination(PageNumberPagination):
    """
    this is for pagination in api

    """

    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 3


class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        it is for filtering data in api
        """

        queryset = Products.objects.all()
        category_name = self.request.query_params.get("category", None)
        name = self.request.query_params.get("name", None)
        search = self.request.query_params.get("search", None)
        min_price = self.request.query_params.get("min_price", None)
        max_price = self.request.query_params.get("max_price", None)

        if name:
            queryset = queryset.filter(name__icontains=name)

        if category_name:
            queryset = queryset.filter(category__name__icontains=category_name)

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(category__name__icontains=search)
            )

        if max_price:
            queryset = queryset.filter(price__gt=max_price)

        if min_price:
            queryset = queryset.filter(price__lt=min_price)

        return queryset


class CategoryView(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class BrandView(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

