from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from classes.models import Class
from .serializers import  ClassSerializer
class StudentListView(APIView):
    def get(self,  request):
        Class = Class.objects.all()
        serializer = ClassSerializer(Class, many=True)
        return Response(serializer.data)
