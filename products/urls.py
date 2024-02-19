from django.urls import include, path
from . import views
from rest_framework import routers


app_name = "products"
router = routers.DefaultRouter()

router.register("products", views.ProductsView, basename="products")
router.register("category", views.CategoryView, basename="category")
router.register("brand", views.BrandView, basename="brand")


urlpatterns = [
    path("", include(router.urls)),
]
