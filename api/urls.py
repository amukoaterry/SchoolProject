from django.urls import path
from .views import (StudentListView, ClassRoomListView, TeacherListView, CourseListView, ClassPeriodListView,  StudentDetailView,  TeacherDetailView, CourseDetailView,  ClassPeriodDetailView, ClassRoomDetailView, TimetableView
)

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student_list_view'),
    path('student/<int:id>/', StudentDetailView.as_view(), name='student_detail_view'),
    
    path('teacher/', TeacherListView.as_view(), name='teacher_list_view'),
    path('teacher/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail_view'),
    path('teacher/<int:teacher_id>/assign-course/', TeacherDetailView.as_view(), name='assign_course'),
    path('teacher/<int:teacher_id>/assign-class/', TeacherDetailView.as_view(), name='assign_class'),
    
    path('course/', CourseListView.as_view(), name='course_list_view'),
    path('course/<int:id>/', CourseDetailView.as_view(), name='course_detail_view'),
    
    path('classroom/', ClassRoomListView.as_view(), name='classroom_list_view'),
    path('classroom/<int:id>/', ClassRoomDetailView.as_view(), name='classroom_detail_view'),
    
    path('classperiod/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
    path('classperiod/<int:id>/', ClassPeriodDetailView.as_view(), name='classperiod_detail_view'),
    path('classperiod/create/', ClassPeriodDetailView.as_view(), name='create_classperiod_with_teacher_and_course'),
    
]
