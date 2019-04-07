from rest_framework import serializers
from .models import University, ProgramHighlights

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'rank', 'university', 'course', 'city', 'location', 'program_highlights')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramHighlights
        fields = ('id', 'start_month', 'class_size',
         'avg_work_experience', 'avg_student_age', 'intl_students',
         'women_students', 'avg_salary', 'scholarship', 'accreditations')