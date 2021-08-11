from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from cbt.models import Subject, Examination
from cbt.forms import ExaminationForm, OptionFormset, QuestionForm


def create_examination(request):
    examinations = Examination.objects.all()
    
    examination_form = ExaminationForm()
    
    form = QuestionForm()
    formset = OptionFormset()


    if request.method == "POST":
        # examination_form = ExaminationForm(request.POST or None)
        # if examination_form.is_valid():
        #     examination_instance = examination_form.save(commit=False)
        #     examination_instance.save()


        form = QuestionForm(request.POST)
        formset = OptionFormset(request.POST)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        
        
        if formset.is_valid():
            formset_instances = formset.save(commit=False)
            for formset_instance in formset_instances:
                formset_instance.question = instance
                formset_instance.save()

            return redirect("create_examination")

        print(form)
        print(formset)

        
        return JsonResponse({"ok": "posted"})

        
    
    ctx ={
        'examinations': examinations,
        'examination_form': examination_form,
        'form': form,
        'formset': formset,
    }
    return render(request, 'cbt/create_examination.html', ctx)


@login_required
def select_course(request):
    """
        select subject combinations of a select a course with multiple subject combinations.
    """
    subjects = Subject.objects.all()

    ctx = {
        'subjects': subjects,
    }
    return render(request, 'cbt/select_course.html', ctx)


@login_required
def exam_hall(request):
    """
        examination starts here students submit answers to there quizzes until
        it's complete or decide to quite.
    """
    pass


@login_required
def final_score(request):
    """
        students are shown final score after validation check if cutoff marks where met.
    """
    pass


@login_required
@require_http_methods(['POST'])
def create_examination_api(request):
    if request.method == "POST":
        examination_form = ExaminationForm(request.POST)
        if examination_form.is_valid():
            instance = examination_form.save(commit=False)
            instance.save()
            examination = model_to_dict(instance)

            return JsonResponse(examination, status=201)
