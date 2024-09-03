
from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/<pk>',student_detail),
    # path('stuinfo/', student_list),
    path('stu/<int:id>/', StudentAPI.as_view()),
]
