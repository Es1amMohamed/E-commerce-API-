from django.urls import include, path
from . import views
from rest_framework import routers


app_name = "products"
router = routers.DefaultRouter()

router.register("", views.ProductsView)
urlpatterns = [
    path("", include(router.urls)),
]
