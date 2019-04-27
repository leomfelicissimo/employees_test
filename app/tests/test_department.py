import json
from rest_framework import status
from django.test import TestCase, RequestFactory
from faker import Faker
from api.serializers import DepartmentSerializer
from api.models import Department
from api.views.department import DepartmentList, DepartmentDetail
from tests.helpers import DepartmentTestHelper

class DepartmentTests(TestCase):
    def setUp(self):
        """Setup common class attributes"""
        self.faker = Faker('pt_BR')
        self.factory = RequestFactory()
        self.json = 'application/json'
        self.url = '/department/'
        self.department = DepartmentTestHelper()

    def test_get_success(self):
        """Should get many departaments"""
        [self.department.create() for _ in range(5)]
        request = self.factory.get(self.url)
        r = DepartmentList.as_view()(request)
        self.assertTrue(len(r.data) == 5)

    def test_get_one_success(self):
        """Should get specific departament"""
        dep = self.department.create_and_get()
        request = self.factory.get(self.url)
        r = DepartmentDetail.as_view()(request, pk=dep.id)
        self.assertNotEqual(r.data, None)

    def test_get_one_not_found(self):
        request = self.factory.get(self.url)
        r = DepartmentDetail.as_view()(request, pk=999)
        self.assertTrue(status.is_client_error(r.status_code))

    def test_create_success(self):
        """Should create new departament"""
        request = self.factory.post(self.url, data={
            'name': 'Dep 1',
            'description': 'Departament Test'
        }, content_type=self.json)
        r = DepartmentList.as_view()(request)
        self.assertTrue(status.is_success(r.status_code))

    def test_create_validation_error(self):
        """Should'nt create new departament returning 400 error"""
        request = self.factory.post(self.url, data={
            'description', 'Departament Test',
        }, content_type=self.json)
        r = DepartmentList.as_view()(request)
        self.assertTrue(status.is_client_error(r.status_code))

    def test_update_success(self):
        """Should update a department data"""
        dep = self.department.create_and_get()
        request = self.factory.put(self.url, data={
            'name': 'Dep Abc1',
            'description': 'Departament Test',
        }, content_type=self.json)
        r = DepartmentDetail.as_view()(request, pk=dep.id)
        self.assertTrue(status.is_success(r.status_code))

    def test_update_not_found(self):
        """Should respond 404 when updating invalid deparment"""
        request = self.factory.put(self.url, data={
            'name': 'Dep Abc1',
            'description': 'Department Test',
        }, content_type=self.json)
        r = DepartmentDetail.as_view()(request, pk=999)
        self.assertTrue(status.is_client_error(r.status_code))
    
    def test_delete_success(self):
        """Should delete a department"""
        dep = self.department.create_and_get()
        request = self.factory.delete(self.url)
        r = DepartmentDetail.as_view()(request, pk=dep.id)
        self.assertTrue(status.is_success(r.status_code))

    def test_delete_not_found(self):
        """Should respond 404 when deleting invalid deparment"""
        request = self.factory.delete(self.url)
        r = DepartmentDetail.as_view()(request, pk=5000)
        self.assertTrue(status.is_client_error(r.status_code))
