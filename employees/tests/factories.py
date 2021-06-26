import factory

from employees.models import Employee


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    name = factory.Faker("name")
    address = factory.Faker("address")
    phone_number = factory.Faker("phone_number")
    salary = factory.Faker("pyint", min_value=500, max_value=1500)
