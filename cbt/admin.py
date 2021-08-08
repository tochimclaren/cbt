from django.contrib import admin
from cbt.models import Question, Subject, Student, Course, Answer

class AnswerInlineAdmin(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]


admin.site.register(Question, QuestionAdmin)

# class SubjectInlineAdmin(admin.TabularInline):
#     model = Subject
#     extra = 0


class CourseAdmin(admin.ModelAdmin):
    # inlines = [SubjectInlineAdmin]
    pass


admin.site.register(Course, CourseAdmin)

admin.site.register(Subject)
admin.site.register(Student)