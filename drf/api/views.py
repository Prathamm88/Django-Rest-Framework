# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student 
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins,generics
# Create your views here.

@api_view(['GET'])
def studentsview(request):
    pass
    # if request.method == 'GET':  
    #     students = Student.objects.all()
    #     serializer = StudentSerializer(students, many=True)
    #     return Response(serializer.data)
    
    # elif request.method == 'POST':
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     print(serializer.errors)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def studentDetailView(request,pk):
    pass
    # try:
    #     student = Student.objects.get(pk=pk)
    # except Student.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET' :
    #     serializer = StudentSerializer(student)
    #     return Response(serializer.data,status=status.HTTP_200_OK) 
    # elif request.method == 'PUT':
    #     serializer = StudentSerializer(student,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
         
    #      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Employees(APIView):
#     def get(self,request):
#         # empployees = Employee.objects.all()
#         # serializer = EmployeeSerializer(empployees,many=True)
#         # return Response(serializer.data, status=status.HTTP_200_OK)
#         pass
   


class EmployeeDetail(APIView):
    def get_object(self,pk):
        pass
    #     try:
    #         return Employee.objects.get(pk=pk)
    #     except Employee.DoesNotExist:
    #         raise Http404   
    # def get(self,request,pk) :
    #     employee = self.get_object(pk)
    #     serializer = EmployeeSerializer(employee)       
    #     return Response (serializer.data, status=status.HTTP_200_OK)
   
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)
     
    def post(self,request):
        return self.create(request)

