from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# @method_decorator(csrf_exempt , name='dispatch')
# class StudentAPI(View):
#     def get(self, request, *args, **kwargs):
#         # Correct way to access the 'id' from kwargs
#         student_id = kwargs.get('id')
#         student = get_object_or_404(Student, id=student_id)
#         serializer = StudentSerializer(student)
#         print(kwargs)
#         return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):
#         # Demonstrate how *args and **kwargs capture arguments
#         response_data = {
#             'args': args,  # This will contain any positional arguments passed
#             'kwargs': kwargs,  # This will contain any named arguments (like from request data or URL)
#             'message': 'Post request received demonstrating *args usage.'
#         }
#         return JsonResponse(response_data, status=status.HTTP_200_OK)
#     def put(self,request,*args,**kwargs):
#         pass
#     def delete(self,request,*args,**kwargs):
#         pass





# def student_detail(request, pk):
    # stu = get_object_or_404(Student,id=pk)
    # stu = Student.objects.get(id=pk)
    # serializer = StudentSerializer(stu)
    # return HttpResponse(stu , content='application/json')
    # return JsonResponse(stu, safe=False)
    # json_data = JSONRenderer().render(serializer.data)
    # return JsonResponse(serializer.data)


# def student_list(request):
#     stu = Student.objects.all();
#     serializer = StudentSerializer(stu , many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data , content_type='application/json')
    # return JsonResponse(serializer.data,safe=False)





