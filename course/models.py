from django.db import models

class Course(models.Model):
   course_name= models.CharField(max_length=20)
   course_code = models.IntegerField()
   teacher = models.CharField(max_length=30)
   number_of_topics = models.IntegerField()
   duration_of_course= models.DateField()
   number_of_students= models.IntegerField()
   description_of_course= models.TextField()
   fees_required= models.IntegerField()
def __str__(self):
       return f"{self.course_name} {self.course_code}"
