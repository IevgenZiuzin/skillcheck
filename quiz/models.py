from django.db import models
from django.core.validators import MinValueValidator
from user.models import QuizAppUser


class QuizCategory(models.Model):
    """
    Quiz category. Superuser creates.
    """
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'QuizCategory'
        verbose_name_plural = 'QuizCategories'


class Quiz(models.Model):
    """
    Quiz. Name 'test' describes it better but is risky and confusing.
    max_score field describes the highest score or rate for quiz with all questions answered correctly
    """
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE, related_name='quizzes')
    creator = models.ForeignKey(QuizAppUser, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=100, unique=True)
    max_score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    """
    Quiz question. is_multi field describes one or multiple options in this question can be correct.
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    title = models.TextField()
    is_multi = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title[:15]}'

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Option(models.Model):
    """
    Quiz option
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    title = models.CharField(max_length=300)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'


class Answer(models.Model):
    """
    Quiz answer. Options from answer and correct options are being compared by checking questions.
    """
    user = models.ForeignKey(QuizAppUser, on_delete=models.CASCADE, related_name='answers')
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='answers')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.option} - {self.date}'

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
