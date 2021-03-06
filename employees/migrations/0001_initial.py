# Generated by Django 3.2.4 on 2021-06-26 21:52

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=20)),
                ("salary", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
