from django.contrib import admin

from .models import Event, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'name', 'email', 'grad_year', 'hours_remaining']

class EventAdmin(admin.ModelAdmin):
  list_display = ['id','name','event_date', 'num_registered', 'get_students']
  list_display_links = ['name']
  filter_horizontal = ('students',)
  
  def get_students(self, instance):
    return [student.name for student in instance.students.all()]


# admin.site.register(Event, EventAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Student, StudentAdmin)