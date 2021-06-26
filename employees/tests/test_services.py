from decimal import Decimal

import pytest

from employees.services import raise_salaries
from employees.tests.factories import EmployeeFactory


@pytest.mark.django_db
class TestRaiseSalary:
    def test_raise_salary(self):
        salary = Decimal("100")
        expected_raised_salary = Decimal("110")

        employee = EmployeeFactory(salary=salary)
        raise_salaries()
        employee.refresh_from_db()
        assert employee.salary == expected_raised_salary

    def test_performance(self, benchmark):
        EmployeeFactory.create_batch(500)

        benchmark(raise_salaries)
