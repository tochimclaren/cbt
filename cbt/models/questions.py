from django.db import models
from django.urls import reverse


class Examination(models.Model):
    title = models.CharField(max_length=200)
    examination_year = models.DateField()
    department = models.ForeignKey('Department', 
        null=True, 
        blank=True, 
        related_name="exam_department", 
        on_delete=models.CASCADE)
    completed_by = models.ManyToManyField('Student', blank=True, related_name='exam_completed_by')
    subjects = models.ForeignKey('Subject', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        related_name="exam_subjects")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "exam_table"
        ordering = ("-examination_year",)

    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=200)


    class Meta:
        db_table = "dept_table"

    def __str__(self):
        return self.title

class Subject(models.Model):
    text = models.CharField(max_length=250)

    class Meta:
        db_table = "subject_table"

    def __str__(self):
        return self.text


class Question(models.Model):
    examination = models.ForeignKey(Examination, 
        blank=True, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name="exam_questions")
    subject = models.ForeignKey(Subject, 
        on_delete=models.CASCADE, 
        related_name="subject_questions")
    text  = models.TextField()
    
    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})

    class  Meta:
        db_table = "question_table"
        ordering = ("text",)

    def __str__(self):
        if self.questions.get(is_correct=True).option:
            return f'{self.questions.get(is_correct=True).option}'
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, 
        related_name="questions")
    option = models.CharField(max_length=512)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question.text}'

    class Meta:
        db_table = "answer_table" 
        ordering = ("option",)