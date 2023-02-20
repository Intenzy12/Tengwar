from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    student_id = models.IntegerField("student id")
    grad_year = models.IntegerField("graduation year")
    hours_remaining = models.IntegerField("hours remaining")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    


class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField("event date")
    num_registered = models.IntegerField("num registered")
    
    def __str__(self):
        return self.name
