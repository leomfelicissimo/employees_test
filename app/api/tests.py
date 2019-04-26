import unittest
import requests
import json
from django import test
from api.serializers import DepartmentSerializer
from api.models import Department
from faker import Faker

def create_fake_employee():
    faker = Faker('pt_BR')
    data = faker.profile(fields=['name', 'mail'])
    return {
        'name': data['name'],
        'email': data['mail'],
        'department_id': 1,
    }


class DepartamentSerializerTests(unittest.TestCase):
    def test_serialization(self):
        department = Department(name="LuizaLabs", description="Department of Technology")
        s = DepartmentSerializer(department)
        self.assertIsNotNone(s.data)

    def test_create(self):
        s = DepartmentSerializer(data={'name': 'Dep 1', 'description': 'Department Number 1'})
        s.is_valid()
        result = s.save()
        self.assertIsNotNone(s)

class EmployeeViewTests(test.TestCase):
    def test_create_new_employee(self):
        url = 'http://localhost:8000/api/employee'
        data = create_fake_employee()
        r = requests.post(url, json=data)
        self.assertEqual(r.status_code, 201)



