from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Employee, Department
from api.serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    # When creating a new employee, is not a good aproach
    # to send a full nested departament with it
    # then 
    def perform_create(self, serializer):
        department = self.request.data['department']
        if (type(department) == int):
            dep = Department.objects.get(pk=department)
        else:
            dep = Department.objects.create(name=str(department))

        serializer.save(department=dep)

class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

