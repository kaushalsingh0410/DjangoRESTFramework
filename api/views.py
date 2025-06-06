from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import StudentSerializer,EmployeeSerializer
from student.models import  Student 
from employee.models import Employee
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from django.http import Http404
from rest_framework import generics,mixins



@api_view(['GET','POST'])
def StudentView(request):
    if request.method == 'GET':
        serializer = StudentSerializer(Student.objects.all(),many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET','PUT','DELETE'])   
def studentAction(request,pk):
    try:
        student = Student.objects.get(pk= pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = StudentSerializer(student)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save() 
        else: 
            return Response(serializer.error,status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data,status = status.HTTP_200_OK)




# # APIView
# class EmployeeList(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees,many = True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)

# class EmployeeACtions(APIView):
#     def getter(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self,request,pk):
#         return Response(EmployeeSerializer(self.getter(pk)).data, status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         slr = EmployeeSerializer(self.getter(pk),data = request.data)
#         if slr.is_valid():
#             slr.save()
#             return Response(slr.data, status = status.HTTP_201_CREATED) 
#         return Response(slr.errors, status = status.HTTP_400_BAD_REQUEST) 
    
#     def delete(self,request,pk):
#         self.getter(pk).delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
        


class EmployeeList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
     