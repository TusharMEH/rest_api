from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer  
from rest_framework import viewsets

# Create your views here.
# class employeeList(APIView):

# 	def get(self,request):
# 		employee1=Employee.objects.all()
# 		serializer=EmployeeSerializer(employee1,many=True)
# 		return Response(serializer.data)

# 	def post(self):
# 		pass

class employeelist(viewsets.ModelViewSet):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer