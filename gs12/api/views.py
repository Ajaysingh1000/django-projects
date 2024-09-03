from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, id=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        # print(request.query_params.get('val'))
        if id is not None:
            # stu = Student.objects.get(id=id)     
            stu = get_object_or_404(Student,id=id)
            serializer = StudentSerializer(stu)
            return Response({'data':serializer.data})
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response({'data':serializer.data})
    
    if request.method=='POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Created Successfully'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        stu = get_object_or_404(Student,id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'data successfully updated'})
        return Response(serializer.errors)
    
    if request.method=='PATCH':
        stu = get_object_or_404(Student,id=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'data successfully updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        stu = get_object_or_404(Student,id=id)
        stu.delete()
        return Response({"message" : "Delete Successfully"})

    

        




        

