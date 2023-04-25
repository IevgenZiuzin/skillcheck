from django.db import models
from user.models import QuizAppUser
from quiz.models import Quiz, QuizCategory


class Completion(models.Model):
    """
    Saves stats information about completion. Created after answers request and checking.
    """
    user = models.ForeignKey(QuizAppUser, on_delete=models.CASCADE, related_name='completions')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='completions')
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE, related_name='completions')
    date = models.DateTimeField(auto_now_add=True)
    total = models.PositiveSmallIntegerField()
    rights = models.PositiveSmallIntegerField()
    max_score = models.PositiveSmallIntegerField()
    percent = models.DecimalField(max_digits=4, decimal_places=1)
    rate = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return f'user:{self.user} quiz:{self.quiz}'

    class Meta:
        verbose_name = 'Completion'
        verbose_name_plural = 'Completions'
