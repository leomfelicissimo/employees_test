from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Employee
from api.serializers import EmployeeSerializer

def get(request):
    emps = Employee.objects.all()
    serializer = EmployeeSerializer(emps, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_one(pk):
    emp = Employee.object.get(pk=pk)
    serializer = EmployeeSerializer(emp, many=False)
    return JsonResponse(serializer.data, safe=False)

def post(request):
    print(request.body)
    data = JSONParser().parse(request)
    serializer = EmployeeSerializer(data=data)
    if (serializer.is_valid()):
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        print('Data is invalid', serializer.errors)
    return JsonResponse(serializer.errors, status=400)

def put(request, pk):
    emp = Employee.objects.get(pk=pk)
    data = JSONParser().parse(request)
    serializer = EmployeeSerializer(emp, data=data)
    if (serializer.is_valid()):
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)

def delete(pk):
    emp = Employee.objects.get(pk=pk)
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