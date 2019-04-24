from django.test import TestCase
from .models import Departament

class DepartamentTests(TestCase):

    def test_create_departament(self):
        d = Departament()
        d.name = "Tech"
        d.description = "Technology Departament" 
        d.save()
        self.assertIs(d.id is None, False)
