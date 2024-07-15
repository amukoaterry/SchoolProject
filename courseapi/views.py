from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from course.models import Course
from .serializer import  CourseSerializer
class CoursetListView(APIView):
    def get(self,  request):
        Course = Course.objects.all()
        serializer = CourseSerializer(Course, many=True)
        return Response(serializer.data)
