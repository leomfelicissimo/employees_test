from api.models import Department, Employee
from faker import Faker

class DepartmentTestHelper():
    def create(self):
        dep = Department()
        dep.name = 'Department Name'
        dep.description = 'Test Description'
        dep.save()

    def create_and_get(self):
        self.create()
        deps = Department.objects.all()
        return deps[0] if len(deps) > 0 else Department()

class EmployeeTestHelper():
    def __init__(self):
        self.department = DepartmentTestHelper()

    def create_fake(self):
        faker = Faker('pt_BR')
        data = faker.profile(fields=['name', 'mail'])
        return {
            'name': data['name'],
            'email': data['mail'],
            'department_id': 1,
        }

    def create(self):
        dep = self.department.create_and_get()
        fake = self.create_fake()
        emp = Employee()
        emp.name = fake['name']
        emp.email = fake['email']
        emp.department = dep
        emp.save()
        return emp

    def create_and_get(self):
        self.create()
        emps = Employee.objects.all()
        return emps[0] if len(emps) > 0 else Employee()
