
from rest_framework import serializers
from classes.models import course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = " __all__ "

    

