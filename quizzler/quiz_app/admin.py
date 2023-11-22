from django.contrib import admin
from .models import Question, Quiz, Score

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_answer')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty')
    filter_horizontal = ('questions',)

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('player', 'quiz', 'score')