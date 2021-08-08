from django.db import models
from django.contrib.auth import get_user_model
from cbt.models.questions import Subject

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    subjects = models.ManyToManyField(Subject)
    enrolled = models.ManyToManyField('Student')

    class Meta:
        db_table = "course_table"
        ordering = ("-created",)

    def __str__(self):  
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    courses = models.ManyToManyField(Course)
    age = models.DateTimeField()
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "student_table"

    def __str__(self):
        return self.user.username


class TestResult(models.Model):
    course = models.ForeignKey(
        Course, 
        blank=True, 
        null=True, 
        on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, 
        blank=True, 
        null=True, 
        on_delete=models.CASCADE)
    score = models.CharField(max_length=10)

    def __str__(self):
        return self.score