from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Employee, Department
from api.serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def perform_create(self, serializer):
        department = self.request.data['department']
        if (type(department) == int):
            print(department)
            dep = Department.objects.get(pk=department)
            serializer.save(department=dep)
        else:
            dep = Department.objects.create(name=str(department))
            serializer.save(department=dep)

class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

