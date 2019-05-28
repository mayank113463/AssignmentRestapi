from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from employees.serializers import EmployeeSerializer
from employees.models import Employee

from employees.pagination import MyPagination



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination
    search_fields = ('first_name','last_name',)
