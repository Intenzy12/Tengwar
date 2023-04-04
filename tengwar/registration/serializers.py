from rest_framework import serializers
from .models import Event, Student, Teacher, Organization

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('pk', 'name', 'email', 'student_id', 'grad_year', 'hours_remaining')