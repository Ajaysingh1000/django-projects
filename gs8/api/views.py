
from .models import *
from .serializer import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView , RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, Allowany



class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # in basic authentcation so when we access localhost it will ask username and password 
    # authentication_classes = [BasicAuthentication]

    # is autheticated ka matlab hai ki authenticated user hi access kar sakta hai 
    # permission_classes  = [IsAuthenticated]

    # allow any matlab koi bhi access kar sakta hai 
    # permission_classes  = [Allowany]
    #check if the user is admin or not 
    # permission_classes  = [IsAdminUser] => is_staff jiska true hoga 

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer






















# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentListCreate(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
