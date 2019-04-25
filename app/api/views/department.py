from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Department
from api.serializers import DepartmentSerializer

def get(request):
    deps = Department.objects.all()
    serializer = DepartmentSerializer(deps, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_one(pk):
    dep = Department.objects.get(pk=pk)
    serializer = DepartmentSerializer(dep, many=False)
    return JsonResponse(serializer.data, safe=False)

def post(request):
    data = JSONParser().parse(request)
    serializer = DepartmentSerializer(data=data)
    if (serializer.is_valid()):
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def put(request, id):
    return HttpResponse(status=500, content="Not implemented")

def delete(pk):
    dep = Department.objects.get(pk=pk)
    dep.delete()
    return HttpResponse(status=204)

@csrf_exempt
def index(request):
    if (request.method == 'GET'):
        return get(request)
    elif (request.method == 'POST'):
        return post(request)

@csrf_exempt
def index_detail(request, pk):
    if (request.method == 'GET'):
        return get_one(pk)
    elif (request.method == 'PUT'):
        return put(request, pk)
    elif (request.method == 'DELETE'):
        return delete(pk)
