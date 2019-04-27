import json
from rest_framework import status
from django.test import TestCase, RequestFactory
from faker import Faker
from api.serializers import EmployeeSerializer
from api.models import Employee, Department
from api.views.employee import EmployeeList, EmployeeDetail
from tests.helpers import DepartmentTestHelper, EmployeeTestHelper

class EmployeeTests(TestCase):
    def setUp(self):
        self.faker = Faker('pt_BR')
        self.factory = RequestFactory()
        self.json = 'application/json'
        self.url = '/employee/'
        self.department = DepartmentTestHelper()
        self.employee = EmployeeTestHelper()

    def test_get_success(self):
        [self.employee.create() for _ in range(5)]
        request = self.factory.get(self.url)
        r = EmployeeList.as_view()(request)
        self.assertTrue(len(r.data) == 5)

    def test_get_one_success(self):
        dep = self.employee.create_and_get()
        request = self.factory.get(self.url)
        r = EmployeeDetail.as_view()(request, pk=dep.id)
        self.assertNotEqual(r.data, None)

    def test_get_one_not_found(self):
        request = self.factory.get(self.url)
        r = EmployeeDetail.as_view()(request, pk=999)
        self.assertTrue(status.is_client_error(r.status_code))

    def test_create_success(self):
        """Should create new employee without errors"""
        dep = self.department.create_and_get()
        request = self.factory.post(self.url, data={
            'name': 'Emp 1',
            'email': 'emp@emp.com.br',
            'department': dep.id,
        }, content_type=self.json)
        r = EmployeeList.as_view()(request)
        self.assertTrue(status.is_success(r.status_code))

    def test_create_validation_error(self):
        """Should'nt create new departament returning 400 error"""
        request = self.factory.post(self.url, data={
            'email', 'emp@emp.com.br'
        }, content_type=self.json)
        r = EmployeeList.as_view()(request)
        self.assertTrue(status.is_client_error(r.status_code))

    def test_update_success(self):
        emp = self.employee.create_and_get()
        request = self.factory.put(self.url, data={
            'id': emp.id,
            'name': 'Employee Abc 1',
            'email': 'employee@gmail.com',
            'department': emp.department.id,
        }, content_type=self.json)
        r = EmployeeDetail.as_view()(request, pk=emp.id)
        self.assertTrue(status.is_success(r.status_code))
    
    def test_delete_success(self):
        emp = self.employee.create_and_get()
        request = self.factory.delete(self.url)
        r = EmployeeDetail.as_view()(request, pk=emp.id)
        self.assertTrue(status.is_success(r.status_code))

    def test_delete_not_found(self):
        request = self.factory.delete(self.url)
        r = EmployeeDetail.as_view()(request, pk=5000)
        self.assertTrue(status.is_client_error(r.status_code))
