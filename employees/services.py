from decimal import Decimal

from django.db import transaction

from .models import Employee


def raise_salaries():
    with transaction.atomic():
        for employee in Employee.objects.all():
            employee.salary *= Decimal("1.1")
            employee.save()
