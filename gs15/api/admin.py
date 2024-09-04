from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' ,'roll' , 'city' , 'passby' ,'file_upload']
