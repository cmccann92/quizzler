from django.urls import path
from . import views

app_name = 'quiz_app'

urlpatterns = [
    path('', views.home, name ='home'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('quiz/<int:quiz_id>/results/', views.results, name='results'),
    path('quiz/<int:quiz_id>/question/<int:question_index>/', views.quiz_question, name='quiz_question'),
    path('quiz/<int:quiz_id>/submit/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('quiz/<int:quiz_id>/results/', views.results, name='results'),
]