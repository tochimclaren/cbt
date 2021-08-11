from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    age = models.DateTimeField()
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "student_table"

    def __str__(self):
        return self.user.username