# Generated by Django 5.0.1 on 2024-03-12 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_remove_products_rating_review"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Review",
        ),
    ]
