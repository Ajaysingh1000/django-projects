from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', LCStudentAPI.as_view()),
    path('stuinfo/<int:pk>/',RUDStudentAPI.as_view()),
    
]