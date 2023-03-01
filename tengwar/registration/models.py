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
    organization_name = models.CharField(max_length=100, null=True)
    event_name = models.CharField(max_length=100, null=True)

    event_description = models.CharField(max_length=250, null=True)
    event_date = models.DateTimeField("event date", null=True)
    event_times = models.CharField(max_length=20, null=True)

    is_recurring = models.BooleanField("is recurring", default=False)
    recursion_type = models.CharField(max_length=100, null=True)

    num_required = models.IntegerField("num required", default=0)
    num_registered = models.IntegerField("num registered", default=0)
    students_registered = models.ManyToManyField(Student)
    # student_contact_id = models.IntegerField("student contact", null=True)
    student_lead = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_lead", null=True)
    
    advisor = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    event_pic_upload = models.ImageField("event_image", upload_to="images/event_image/", null=True)
    logo_upload = models.ImageField("logo", upload_to="images/logo/", null=True)
    
    def __str__(self):
        return self.event_name
