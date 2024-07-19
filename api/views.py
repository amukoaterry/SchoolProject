from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from student.models import Student
from .serializers import  StudentSerializer
from .serializers import CourseSerializer
from .serializers import TeacherSerializer
from .serializers import ClassRoomSerializer
from .serializers import ClassPeriodSerializer

class StudentListView(APIView):
    def get(self,  request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):

        
        def get(self,request,id):
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        
        
        
        def put(self,request,id):
            student =Student.objects.get(id=id)
            serializer=StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.Save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            





            


class CourseListView(APIView):
    def get(self,  request):
        Course = Course.objects.all()
        serializer = CourseSerializer(Course, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
        
    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    






    
    
class TeacherListView(APIView):
    def get(self,  request):
        teacher = TeacherListView.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
        
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







    
class ClassRoomListView(APIView):
    def get(self,  request):
        classroom = ClassRoomListView.objects.all()
        serializer = ClassRoomSerializer(classroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class ClassRoomDetailView(APIView):
    def get(self, request, id):
        classroom = ClassRoom.objects.get(id=id)
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)
        
    def put(self, request, id):
        classroom = ClassRoom.objects.get(id=id)
        serializer = ClassRoomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        classroom = ClassRoom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




    
    
    
class ClassPeriodListView(APIView):
    def get(self,  request):
        classperiod = ClassPeriodListView.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod = Classperiod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
        
    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

             
    
  