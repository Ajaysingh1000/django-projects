
from rest_framework import serializers
from .models import *


class SingerSerializer(serializers.ModelSerializer):
    # ye field read only hi hota hai 
    # song = serializers.StringRelatedField(many=True, read_only = True)
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='duration')
    song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id' , 'title' , 'singer' , 'duration']