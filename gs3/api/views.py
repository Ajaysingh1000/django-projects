from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentSerializer
from .models import *


@api_view(['GET'])
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    serializer = StudentSerializer(student)  
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT' , 'PATCH'])
def student_update(request, id):
    data = get_object_or_404(Student,id=id)
    partial = request.method == 'PATCH'
    serializer = StudentSerializer(data, data=request.data,partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg' : "update successfully"} , status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request,id):
    data = get_object_or_404(Student, id=id)
    data.delete()
    return Response({'msg':"deleted successfully"}, status=status.HTTP_200_OK)



