# Generated by Django 4.2.6 on 2023-12-13 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Amazone", "0003_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(default="", max_length=200, null=True)),
                ("mobile", models.BigIntegerField()),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("status", models.BooleanField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Amazone.registrations",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Amazone.product",
                    ),
                ),
            ],
        ),
    ]
