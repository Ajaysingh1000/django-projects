#GenericAPIView and model mixin
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin


# get all students
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        #list method is already implemented in ListModelMixin
        return self.list(request,*args,**kwargs)
    

# create student
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request,*args,**kwargs):
        #list method is already implemented in ListModelMixin
        return self.create(request,*args,**kwargs)

#retrieve particular student 
class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        #list method is already implemented in ListModelMixin
        return self.retrieve(request,*args,**kwargs)
    

#update the student
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self,request,*args,**kwargs):
        #list method is already implemented in ListModelMixin
        return self.update(request,*args,**kwargs)
    

#delete a student
class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self,request,*args,**kwargs):
        #list method is already implemented in ListModelMixin
        return self.destroy(request,*args,**kwargs)
    

