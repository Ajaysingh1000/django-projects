#GenericAPIView and model mixin
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin


# List and Create - PK Not required
class LCStudentAPI(GenericAPIView,ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        #list method is already implemented in ListModelMixin
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        #create method is already implemented in CreateModelMixin
        return self.create(request,*args,**kwargs)

#retrieve update and destroy - PK is required 
class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        #retrieve method is already implemented in RetrieveModelMixin
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        #update method is already implemented in UpdateModelMixin
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        #destroy method is already implemented in DestroyModelMixin
        return self.destroy(request,*args,**kwargs)
    

