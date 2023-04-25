from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Quiz, QuizCategory, Question, Option, Answer
from stats.models import Completion
from .serializers import (QuizCategorySerializer,
                          QuizSerializer,
                          StudentQuizSerializer,
                          QuestionSerializer,
                          OptionSerializer,
                          AnswerSerializer)
from stats.serializers import CompletionSerializer
from .filters import QuizFilter, QuestionFilter, OptionFilter, AnswerFilter
from user.permissions import IsModerator, IsStudent
from .service import check_quiz


class QuizCategoryViewSet(viewsets.ModelViewSet):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filterset_class = QuizFilter
    permission_classes = [IsModerator]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class QuizStudentViewSet(QuizViewSet):
    queryset = Quiz.objects.filter(is_draft=False)
    serializer_class = QuizSerializer
    filterset_class = QuizFilter
    permission_classes = [IsStudent]
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        """
        :return: quiz with nested question list nested options list without is_right option fields
        """
        self.queryset = Quiz.objects.prefetch_related('questions__options')
        self.serializer_class = StudentQuizSerializer
        return super().retrieve(request, *args, **kwargs)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.prefetch_related('options').all()
    serializer_class = QuestionSerializer
    permission_classes = [IsModerator]
    filterset_class = QuestionFilter


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsModerator]
    filterset_class = OptionFilter


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsModerator]
    filterset_class = AnswerFilter
    http_method_names = ['get']


class AnswerStudentViewSet(AnswerViewSet):
    permission_classes = [IsStudent]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        """
        Creates answers instances, checks quiz and creates completions with calculated check data
        """
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        answers_instances = serializer.create(serializer.validated_data)
        if answers_instances:
            quiz_result = check_quiz(answers_instances)
            completion = Completion.objects.create(
                user=request.user,
                quiz=quiz_result['quiz'],
                category=quiz_result['category'],
                total=quiz_result['total'],
                rights=quiz_result['rights'],
                max_score=quiz_result['max_score'],
                percent=quiz_result['percent'],
                rate=quiz_result['rate'],
            )
            result = CompletionSerializer(completion)
            return Response(result.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
