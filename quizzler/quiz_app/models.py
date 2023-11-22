from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_one = models.CharField(max_length=255)
    option_two = models.CharField(max_length=255)
    option_three = models.CharField(max_length=255)
    option_four = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)
    category = models.CharField(max_length=255, blank=True)
    difficulty = models.CharField(max_length=255, choices = [('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])

    def __str__(self):
        return self.title

class Score(models.Model):
    player = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.player}'s score on {self.quiz.title}: {self.score}"
    
    