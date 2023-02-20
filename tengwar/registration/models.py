from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    student_id = models.IntegerField("student id")
    grad_year = models.IntegerField("graduation year")
    hours_remaining = models.IntegerField("hours remaining")

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    

class Event(models.Model):
    event_date = models.DateTimeField(("event date"), auto_now=False, auto_now_add=False)