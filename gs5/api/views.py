from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.



class StudentAPI(APIView):
    def get(self,request,id=None,format=None):
        if id is not None:
            # stu = Student.objects.get(id=id)     
            stu = get_object_or_404(Student,id=id)
            serializer = StudentSerializer(stu)
            return Response({'data':serializer.data})
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response({'data':serializer.data})
    
    def post(self,request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Created Successfully'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,format=None):
        stu = get_object_or_404(Student,id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'data successfully updated'})
        return Response(serializer.errors)
    
    def patch(self,request,id,format=None):
        stu = get_object_or_404(Student,id=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'data successfully updated'})
        return Response(serializer.errors)
    
    def delete(self,request,id,format=None):
        stu = get_object_or_404(Student,id=id)
        stu.delete()
        return Response({"message" : "Delete Successfully"})
        
    

        




        

