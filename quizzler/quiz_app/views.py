from django.shortcuts import render, redirect
from .models import Quiz, Question, Score

def home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_app/home.html', {'quizzes':quizzes})

def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    request.session['quiz_id'] = quiz_id
    request.session['question_index'] = 0
    request.session['score'] = 0
    return redirect('quiz_app:quiz_question', quiz_id=quiz_id, question_index=0)

def quiz_question(request, quiz_id, question_index):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = list(quiz.questions.all())
    question = questions[question_index]

    context = {
        'quiz':quiz,
        'question':question,
        'question_index':question_index,
        'total_questions':len(questions)
    }
    return render(request, 'quiz_app/quiz_question.html',context)

from django.shortcuts import get_object_or_404, redirect

def submit_answer(request, quiz_id, question_id):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_id)
        selected_option = request.POST.get('answer')
        correct_answer = question.correct_answer

        if selected_option == correct_answer:
            request.session['score'] = request.session.get('score', 0) + 1

        # Get the quiz object
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        # Get the list of questions associated with this quiz
        questions = list(quiz.questions.all())
        # Find out the current index of the question
        current_index = questions.index(question)

        # If there are more questions, go to the next one
        if current_index + 1 < len(questions):
            next_question = questions[current_index + 1]
            return redirect('quiz_app:quiz_question', quiz_id=quiz.id, question_index=current_index + 1)
        else:
            # No more questions, show results
            return redirect('quiz_app:results', quiz_id=quiz.id)

    # If not a POST request or some other issue, redirect to the current question
    return redirect('quiz_app:quiz_question', quiz_id=quiz_id, question_index=question_id)


def results(request, quiz_id):
    score = request.session.get('score', 0)
    total_questions = len(Quiz.objects.get(id=quiz_id).questions.all())

    request.session['quiz_id'] = None
    request.session['question_index'] = None
    request.session['score'] = 0

    context = {
        'score':score,
        'total_questions': total_questions
    }
    return render(request, 'quiz_app/results.html', context)
