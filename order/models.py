from django.db import models
from operator import mod
from django.contrib.auth.models import User
from products.models import Products

# Create your models here.


ORDER_STATUS = (
    ("Pending", "Pending"),
    ("Out for delivery", "Out for delivery"),
    ("Delivered", "Delivered"),
)

PAYMENT_STATUS = (
    ("Pending", "Pending"),
    ("Done", "Done"),
)

PAYMENT_METHOD = (
    ("Cash on delivery", "Cash on delivery"),
    ("Cridit card", "Cridit card"),
)


class Order(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    total_amount = models.IntegerField(default=0)
    order_status = models.CharField(
        max_length=50, choices=ORDER_STATUS, default="Pending"
    )
    payment_status = models.CharField(
        max_length=30, choices=PAYMENT_STATUS, default="Pending"
    )
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_METHOD, default="Cash on delivery"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
