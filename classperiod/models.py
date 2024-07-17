from django.db import models


class ClassPeriod(models.Model):
  start_time= models.TimeField(max_length=20)
  end_time= models.TimeField()
  courses= models.CharField(max_length=25)
  classroom= models.TextField()
  day_of_the_week = models.TextField()


def __str__(self):
  return f"{self.start_time} {self.end_time}"

