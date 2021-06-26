from uuid import uuid4

from django.db import models


class Employee(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(null=False, max_length=100)
    address = models.TextField(null=False, max_length=500)
    phone_number = models.CharField(null=False, max_length=50)
    salary = models.DecimalField(null=False, decimal_places=2, max_digits=6)
