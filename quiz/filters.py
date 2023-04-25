from quiz.models import Quiz, Question, Option, Answer
from django_filters import rest_framework as filters


class QuizFilter(filters.FilterSet):

    class Meta:
        model = Quiz
        fields = ['category', 'creator', 'is_draft']


class QuestionFilter(filters.FilterSet):

    class Meta:
        model = Question
        fields = ['quiz']


class OptionFilter(filters.FilterSet):

    class Meta:
        model = Option
        fields = ['question', 'is_right']


class AnswerFilter(filters.FilterSet):

    class Meta:
        model = Answer
        fields = ['user', 'date']

