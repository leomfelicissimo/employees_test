from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import bad_request
from api.models import Employee, Department
from api.serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    # When creating a new employee, is not a good aproach
    # to send a full nested departament with it
    def perform_create(self, serializer):
        department = self.request.data.get('department', None)

        if (type(department) == int):
            dep = Department.objects.get(pk=department)
        else:
            name = str(department)
            try:
                dep = Department.objects.get(name=name)
            except Department.DoesNotExist:
                dep = Department.objects.create(name=name)
            except Department.MultipleObjectsReturned:
                dep = Department.objects.filter(name=name).first()

        if serializer.is_valid(raise_exception=True):
            serializer.save(department=dep)

class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

