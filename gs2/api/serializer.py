from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # def create(self , validated_data):
    #     print(type(validated_data))
    #     return Student.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    # # Update the fields if they are present in the validated data
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.save()  # Save the updated instance
    #     return instance

    # Field level Validation
    # def validate_roll(self, value):
    #     if (value >= 200):
    #         raise serializers.ValidationError('Seat Full')
    #     return value
   
    #object level validation 
    def validate(self, data):    
        nm = data.get("name")
        ct = data.get("city")
        if nm.lower()=='rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be ranchi')
        return data


