from unittest import TestCase
from api.serializers import DepartmentSerializer
from api.models import Departament

class DepartamentSerializerTests(TestCase):
    def test_serialization(self):
        department = Departament(name="LuizaLabs", description="Department of Technology")
        s = DepartmentSerializer(department)
        self.assertIsNotNone(s.data)

    def test_create(self):
        s = DepartmentSerializer(data={'name': 'Dep 1', 'description': 'Department Number 1'})
        s.is_valid()
        result = s.save()
        self.assertIsNotNone(s)

