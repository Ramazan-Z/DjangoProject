# Generated by Django 5.1 on 2024-09-10 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "title",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=150,
                        unique=True,
                        verbose_name="Наиенование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Введите описание категории", null=True, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "db_table": "category",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "title",
                    models.CharField(
                        help_text="Введите наименование товара", max_length=150, verbose_name="Наиенование"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Введите описание товара", null=True, verbose_name="Описание"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение товара",
                        null=True,
                        upload_to="images/",
                        verbose_name="Изображение",
                    ),
                ),
                ("price", models.IntegerField(help_text="Введите цену товара", verbose_name="Цена")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="products", to="catalog.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "db_table": "product",
                "ordering": ["title"],
            },
        ),
    ]