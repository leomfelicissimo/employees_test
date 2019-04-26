from django.urls import path
from api.views import department, employee

urlpatterns = [
    path('department', department.index, name='index'),
    path('department/<int:pk>', department.index_detail, name='index_detail'),
    path('employee', employee.index, name='index'),
    path('employee/<int:pk>', employee.index_detail, name='index_detail')
]