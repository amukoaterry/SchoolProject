from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from classperiod.models import ClassPeriod
from classroom.models import Classroom
from course.models import Course
from student.models import Student
from teacher.models import Teacher
from .serializers import StudentSerializer, CourseSerializer, TeacherSerializer, ClassRoomSerializer, ClassPeriodSerializer


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        country = request.query_params.get("country")
        first_name = request.query_params.get("first_name")

        if country:
            students = students.filter(country=country)
        if first_name:
            students = students.filter(first_name=first_name)

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def enroll_student(self, request, course_id):
        student_id = request.data.get("student_id")
        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)
        student.courses.add(course)
        return Response(status=status.HTTP_200_OK)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def assign_course(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course_id = request.data.get("course_id")
        course = Course.objects.get(id=course_id)
        course.teacher = teacher
        course.save()
        return Response(status=status.HTTP_200_OK)

    def assign_class(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        class_id = request.data.get("class_id")
        classroom = Classroom.objects.get(id=class_id)
        classroom.teacher = teacher
        classroom.save()
        return Response(status=status.HTTP_200_OK)


class ClassRoomListView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassRoomSerializer(classrooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassRoomDetailView(APIView):
    def get(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)

    def put(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassRoomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)

    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create_with_teacher_and_course(self, request):
        teacher_id = request.data.get("teacher_id")
        course_id = request.data.get("course_id")
        classroom_id = request.data.get("classroom_id")

        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        classroom = Classroom.objects.get(id=classroom_id)

        classperiod = ClassPeriod.objects.create(
            teacher=teacher,
            course=course,
            classroom=classroom,
            **request.data
        )
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TimetableView(APIView):
    def get(self, request, classroom_id):
        classperiods = ClassPeriod.objects.filter(classroom_id=classroom_id)
        timetable = {}

        for period in classperiods:
            day = period.day_of_week
            if day not in timetable:
                timetable[day] = []
            timetable[day].append({
                "period": period.period,
                "course": period.course.name,
                "teacher": period.teacher.name,
                "classroom": period.classroom.name,
            })

        return Response(timetable, status=status.HTTP_200_OK)
