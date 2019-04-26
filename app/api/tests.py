import json
from django.test import TestCase, RequestFactory
from faker import Faker
from api.serializers import DepartmentSerializer
from api.models import Department
from api.views.department import DepartmentView


class DepartmentViewTests(TestCase):
    def setUp(self):
        self.faker = Faker('pt_BR')
        self.factory = RequestFactory()
        self.json = 'application/json'
        self.url = '/department/'

    def test_get_success(self):
        request = self.factory.get(self.url)
        r = DepartmentView.as_view()(request)
        self.assertEqual(r.status_code, 200)

    def test_create_success(self):
        """Should create new departament without errors"""
        request = self.factory.post(self.url, data={
            'name': 'Dep 1',
            'description': 'Departament Test'
        }, content_type=self.json)
        r = DepartmentView.as_view()(request)
        self.assertEqual(r.status_code, 201)

    def test_create_validation_error(self):
        """Should'nt create new departament returning 400 error"""
        request = self.factory.post(self.url, data={
            'description', 'Departament Test'
        }, content_type=self.json)
        r = DepartmentView.as_view()(request)
        self.assertEqual(r.status_code, 400)

    def test_update_success(self):
        dep = Department()
        dep.name = 'Dep 1'
        dep.description = 'Teste'
        dep.save()
        deps = Department.objects.all()

        request = self.factory.put(self.url, data={
            'name': 'Dep Abc1',
            'description': 'Departament Test'
        }, content_type=self.json)
        r = DepartmentView.as_view()(request, deps[0].id)
        self.assertEqual(r.status_code, 200)

class EmployeeViewTests(TestCase):
    EMPLOYEE_ENDPOINT = 'http://localhost:8000/api/employee/'

    def create_fake_employee():
        faker = Faker('pt_BR')
        data = faker.profile(fields=['name', 'mail'])
        return {
            'name': data['name'],
            'email': data['mail'],
            'department_id': 1,
        }

    def test_post_new_employee(self):
        print('Should Post Without Error')
        data = self.create_fake_employee()
        r = requests.post(self.EMPLOYEE_ENDPOINT, json=data)
        self.assertEqual(r.status_code, 201)



