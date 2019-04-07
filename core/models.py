from django.db import models

# Create your models here.


class ProgramHighlights(models.Model):
    start_month = models.CharField(max_length=50)
    class_size = models.CharField(max_length=50)
    avg_work_experience = models.CharField(max_length=50)
    avg_student_age = models.CharField(max_length=50)
    intl_students = models.CharField(max_length=50)
    women_students = models.CharField(max_length=50)
    avg_salary = models.CharField(max_length=50, null=True, blank=True)
    scholarship = models.CharField(max_length=50)
    accreditations = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.id


class University(models.Model):
    rank = models.IntegerField()
    university = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    more = models.CharField(max_length=200)
    program_highlights = models.OneToOneField(
        ProgramHighlights, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.university
