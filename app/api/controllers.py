from django.http import HttpResponse

def post(request):
    print(request.body)
def index(request):
    if (request.method == 'POST'): post(request)
    return HttpResponse('Get All Employes')