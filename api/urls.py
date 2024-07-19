from django.urls import path
from .views import StudentListView
from .views import ClassRoomListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassPeriodListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views  import CourseDetailView
from .views import ClassPeriodDetailView
from .views import ClassRoomDetailView


urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view'),
    path('teacher/', TeacherListView.as_view(), name = 'teacher_list_view'),
    path('course/', CourseListView.as_view(), name = 'course_list_view'),
    path('classroom/', ClassRoomListView.as_view(), name = 'classroom_list_view'),
    path('classperiod/', ClassPeriodListView.as_view(), name = 'classperiod_list_view'),
    path('student/<int:id>/', StudentDetailView.as_view(), name='student_detail_view'),
    path('course/<int:id>/', CourseDetailView.as_view(), name='course_detail_view'),
    path('teacher/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail_view'),
    path('classperiod/<int:id>/', ClassPeriodDetailView.as_view(), name='course_detail_view'),
    path('classroom/<int:id>/', ClassRoomDetailView.as_view(), name='course_detail_view'),


]


