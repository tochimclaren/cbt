from django import forms
from django.conf import settings
from django.forms import formset_factory
from .models import Examination, Subject, Question, Answer


class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['title', 'department', 'examination_year', 'subjects']

class SubjectSelectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['text']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['option','is_correct']

OptionFormset = formset_factory(AnswerForm, extra=4, max_num=settings.MAX_NUM)


