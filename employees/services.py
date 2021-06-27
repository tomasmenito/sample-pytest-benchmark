from django.db import transaction
from django.db.models import F

from .models import Employee


def raise_salaries():
    with transaction.atomic():
        Employee.objects.update(salary=F("salary") * 1.1)
