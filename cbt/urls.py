from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_course, name="select_courses"),
    path('create_examination/', views.create_examination, 
                                name="create_examination"),
    path('exam_hall/', views.exam_hall, name="exam_hall"),
    path('final_score/', views.final_score, name="final_score"),

    path('api/create-examination', views.create_examination_api, 
                                name="create_examination_api"),
]