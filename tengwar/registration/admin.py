from django.contrib import admin

from .models import Event, Student, Teacher, Organization


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "student_id",
        "name",
        "email",
        "grad_year",
        "hours_remaining",
    ]


class EventAdmin(admin.ModelAdmin):
    list_display = [
        "organization_name",
        "event_name",
        "event_time",
        "event_duration",
        "event_end_time",
        "event_description",
        "is_recurring",
        "recursion_type",
        "num_required",
        "get_students_registered",
    ]
    list_display_links = ["event_name"]
    filter_horizontal = ("students_registered",)

    def get_students_registered(self, instance):
        return [student.name for student in instance.students_registered.all()]


admin.site.register(Event, EventAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Organization)
