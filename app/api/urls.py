from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.employee import EmployeeList, EmployeeDetail
from api.views.department import DepartmentList, DepartmentDetail

urlpatterns = [
    path('department/', DepartmentList.as_view()),
    path('department/<int:pk>', DepartmentDetail.as_view()),
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>', EmployeeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)