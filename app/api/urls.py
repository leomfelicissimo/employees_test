from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.employee import EmployeeView
from api.views.department import DepartmentView

urlpatterns = [
    path('department/', DepartmentView.as_view()),
    path('department/<int:pk>', DepartmentView.as_view()),
    path('employee/', EmployeeView.as_view()),
    path('employee/<int:pk>', EmployeeView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)