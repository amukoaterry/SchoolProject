from django.urls import path, include
from .views      import ClassListView
urlpatterns = [
    path('class/', ClassListView.as_view(), name = 'class_list_view')
]