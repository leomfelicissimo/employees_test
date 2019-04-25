from django.urls import path
from api.views import department

urlpatterns = [
    path('department', department.index, name='index'),
    path('department/<int:pk>', department.index_detail, name='index')
]