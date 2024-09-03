from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/', StudentList.as_view()),
    path('stuinfo/', StudentCreate.as_view()),
    # path('stuinfo/<int:pk>/',StudentRetrieve.as_view()),
    # path('stuinfo/<int:pk>/',StudentUpdate.as_view()),
    path('stuinfo/<int:pk>/',StudentDestroy.as_view()),
    
]