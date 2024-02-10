# Generated by Django 5.0.1 on 2024-02-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Exam",
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
                ("name", models.CharField(max_length=30)),
                ("image", models.TextField()),
                ("description", models.TextField()),
                ("authorName", models.CharField(max_length=30)),
                ("authorPhoneNum", models.CharField(max_length=11)),
                ("rating", models.FloatField()),
                ("difficulty", models.CharField(max_length=15)),
                ("grade", models.CharField(max_length=7)),
                ("price", models.IntegerField()),
                ("isVerified", models.BooleanField(default=False)),
            ],
        ),
    ]
