from django.db import models
from django.urls import reverse

class Subject(models.Model):
    text = models.CharField(max_length=250)

    class Meta:
        db_table = "subject_table"

    def __str__(self):
        return self.text


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    text  = models.TextField()
    
    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})

    class  Meta:
        db_table = "question_table"
        ordering = ("text", )

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