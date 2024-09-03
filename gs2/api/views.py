# from django.shortcuts import render
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from .serializer import *
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.


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





# @csrf_exempt 
# def student_create(request):
#     if (request.method=='POST'):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data)
        
