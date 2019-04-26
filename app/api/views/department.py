from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, APIException
from django.http import Http404
from api.models import Department
from api.serializers import DepartmentSerializer

class DepartmentView(APIView):
    def get(self, request, format=None):
        deps = Department.objects.all()
        serializer = DepartmentSerializer(deps, many=True)
        return Response(serializer.data)

    def get_object(self, request, pk, format=None):
        try:
            dep = Department.objects.get(pk=pk)
            serializer = DepartmentSerializer(dep, many=False)
            return Response(serializer.data)
        except Department.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk, format=None):
        data = JSONParser().parse(request)
        dep = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(dep, data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        dep = Department.objects.get(pk=pk)
        dep.delete()
        return Response(status=204)