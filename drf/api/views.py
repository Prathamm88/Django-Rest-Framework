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
from rest_framework import mixins,generics,viewsets
from blog.serilizers import BlogSerializer,commentSerializer
from blog.models import Blog,comment
from .pagination import CustomPagination
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

@api_view(['GET'])
def studentsview(request):
    pass
    if request.method == 'GET':  
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def studentDetailView(request,pk):
    pass
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' :
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Employees(APIView):
#     def get(self,request):
#         empployees = Employee.objects.all()
#         serializer = EmployeeSerializer(empployees,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
   


# class EmployeeDetail(APIView):
#     def get_object(self,pk):
#         pass
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404   
#     def get(self,request,pk) :
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)       
#         return Response (serializer.data, status=status.HTTP_200_OK)

# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self,request):
#         return self.list(request)
     
#     def post(self,request):
#         return self.create(request)


class EmployeeDetail(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     generics.GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    

    def put(self,reuqest,pk):
        return self.update(reuqest,pk) 
    
    def delete(self,request,pk):
        return self.destroy(request,pk)


# class EmployeeViewset(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response (serializer.errors)
    

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_fields = ['designation','emp_name','id']

class EmployeeSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_body']
    ordering_fieds = ['id']

class  commentsView(generics.ListCreateAPIView):
    queryset = comment.objects.all()
    serializer_class = commentSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class commentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    pass
#     queryset = comment.objects.all()
#     serializer_class = commentSerializer