from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Student
from .serializer import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class StudentListView(ListAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    

    @swagger_auto_schema(
        operation_description="Upload student data with a file",
        request_body=StudentSerializer,
        # manual_parameters=[
        #     openapi.Parameter(
        #         name='file_upload',
        #         in_=openapi.IN_HEADER,
        #         description="Upload a PDF file",
        #         type=openapi.TYPE_FILE,
        #         required=True,
        #     )
        # ],
        responses={201: StudentSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['roll']
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
    #  def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return Purchase.objects.filter(purchaser=user)




    
    # def get_queryset(self):
    #     user = self.request.user
    #     print(user)
    #     return Student.objects.filter(passby=user)
    