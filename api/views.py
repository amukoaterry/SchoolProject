from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import  StudentSerializer
from .serializers import CourseSerializer
from .serializers import ClassRoomSerializer
from .serializers import ClassPeriodSerializer

class StudentListView(APIView):
    def get(self,  request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)


class CourseListView(APIView):
    def get(self,  request):
        Course = Course.objects.all()
        serializer = CourseSerializer(Course, many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self,  request):
        Teacher = Teacher.objects.all()
        serializer = StudentSerializer(Teacher, many=True)
        return Response(serializer.data)
    
class ClassRoomListView(APIView):
    def get(self,  request):
        classroom = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classroom, many=True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self,  request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)