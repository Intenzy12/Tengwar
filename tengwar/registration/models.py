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
    
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'image/{0}/{1}'.format(instance.name, filename)

class Event(models.Model):
    organization_name = models.CharField(max_length=100, null=True)
    event_name = models.CharField(max_length=100, null=True)
    event_description = models.CharField(max_length=250, null=True)
    event_date = models.DateTimeField("event date", null=True)
    event_times = models.CharField(max_length=20, null=True)
    is_recurring = models.BooleanField("is recurring", null=False, default=False)
    recursion_type = models.CharField(max_length=100, null=True)
    num_students_needed = models.IntegerField("num needed", null=False, default=0)
    num_registered = models.IntegerField("num registered", null=False, default=0)
    students_registered = models.CharField(max_length=500, null=True)
    student_contact_id = models.IntegerField("student contact", null=True)
    logo_upload = models.ImageField(upload_to=user_directory_path, null=True)
    event_pic_upload = models.ImageField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return self.name