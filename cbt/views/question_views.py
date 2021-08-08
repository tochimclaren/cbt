from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cbt.models import Question


def select_course(request):
    """
        select subject combinations of a select a course with multiple subject combinations.
    """
    pass


def exam_hall(request):
    """
        examination starts here students submit answers to there quizzes until
        it's complete or decide to quite.
    """
    pass


def final_score(request):
    """
        students are shown final score after validation check if cutoff marks where met.
    """
    pass