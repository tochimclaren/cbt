from django.db import models
from . import Course

class Subject(models.Model):
    text = models.TextField()
    course = models.ManyToManyField(
        Course, 
        related_name="courses_subjects")

    class Meta:
        db_table = "subject_table"


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    text  = models.TextField()

    class  Meta:
        db_table = "question_table"
        ordering = ("text", )


class Answer(models.Model):
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, 
        related_name="questions")
    option = models.TextField()
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = "answer_table" 
        ordering = ("option",)