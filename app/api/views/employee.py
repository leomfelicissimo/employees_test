from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Employee
from api.serializers import EmployeeSerializer
from rest_framework.views import APIView

class EmployeeView(APIView):

    def get(self, request):
        emps = Employee.objects.all()
        return Response(emps)