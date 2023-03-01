from django.contrib import admin

from .models import Event, Student

class StudentAdmin(admin.ModelAdmin):
  list_display = ['student_id', 'name', 'email', 'grad_year', 'hours_remaining']

class EventAdmin(admin.ModelAdmin):
  list_display = ['organization_name','event_name','event_date', 'event_times', 'num_registered', 'event_description', 'is_recurring', 'recursion_type', 'num_students_needed', 'num_registered', 'students_registered', 'student_contact_id', 'logo_upload', 'event_pic_upload']
  ##list_display_links = ['name']
  
  ##def get_students(self, instance):
    ##return [student.name for student in instance.students.all()]


# admin.site.register(Event, EventAdmin)
# admin.site.register(Student, StudentAdmin)