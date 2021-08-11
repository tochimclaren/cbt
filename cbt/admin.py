from django.contrib import admin
from cbt.models import Examination, Question, Subject, Student, Answer, Department

class AnswerInlineAdmin(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]


admin.site.register(Question, QuestionAdmin)

# class SubjectInlineAdmin(admin.TabularInline):
#     model = Subject
#     extra = 0


class ExaminationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Examination, ExaminationAdmin)


admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Department)