

from rest_framework import serializers
from .models import *


class StudentSerializer (serializers.ModelSerializer):

    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.Va1idationError( 'Name should be start with R')
    #explicity define the field if do any validation


    name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name']
        # extra_kwargs = {'name' : {'read_only':True}}
    
    #field level validation
    def validate_roll(self , value):
        if (value>=200):
            raise serializers.ValidationError("roll must less than 200")
        return value
    
    #object level validation 
    def validate(self, data):    
        nm = data.get("name")
        ct = data.get("city")
        if nm.lower()=='rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be ranchi')
        return data
    
    
    
