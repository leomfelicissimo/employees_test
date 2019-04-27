from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, ParseError
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, APIException
from django.http import Http404

class CRUDView:
    def __init__(self, model, serializer):
        self.model = model
        self.serializer = serializer

    def get(self, request, pk=None, format=None):
        if (pk != None):
            return self.get_object(request, pk, format)
        objs = self.model.objects.all()
        serializer = self.serializer(objs, many=True)
        return Response(serializer.data)

    def get_object(self, request, pk, format=None):
        try:
            obj = self.model.objects.get(pk=pk)
            serializer = self.serializer(obj, many=False)
            return Response(serializer.data)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        try:
            data = JSONParser().parse(request)
            serializer = self.serializer(data=data)
            if (serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ParseError as err:
            print(err)

    def put(self, request, pk, format=None):
        try:
            data = JSONParser().parse(request)
            obj = self.model.objects.get(pk=pk)
            serializer = self.serializer(obj, data=data)
            if (serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            obj = self.model.objects.get(pk=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)