from django.db.models import Count, Avg

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from user.permissions import IsModerator, IsStudent
from .models import Completion
from .serializers import CompletionSerializer
from .filters import CompletionFilter, StudentCompletionFilter


class ModeratorCompletionViewSet(viewsets.ModelViewSet):
    queryset = Completion.objects.all()
    serializer_class = CompletionSerializer
    filterset_class = CompletionFilter
    permission_classes = [IsModerator]
    http_method_names = ['get']

    @action(detail=False)
    def stats(self, request):
        """
        :return: 0 for no completions queryset and annotated and aggregated data, depending on filters used by request
        """
        queryset = self.filter_queryset(self.get_queryset())
        completions_quantity = queryset.count()
        categories_quantity = users_quantity = quizzes_quantity = avg_rights_percent = 0
        if completions_quantity > 0:
            categories_quantity = queryset.annotate(cat_quant=Count('category')).first().cat_quant
            users_quantity = queryset.annotate(user_quant=Count('user')).first().user_quant
            quizzes_quantity = queryset.annotate(quiz_quant=Count('quiz')).first().quiz_quant
            avg_rights_percent = queryset.aggregate(Avg('percent'))['percent__avg']
        result = {
            'completions_quantity': completions_quantity,
            'categories_quantity': categories_quantity,
            'users_quantity': users_quantity,
            'quizzes_quantity': quizzes_quantity,
            'avg_rights_percent': avg_rights_percent,
        }
        return Response(result)


class StudentCompletionViewSet(ModeratorCompletionViewSet):
    permission_classes = [IsStudent]
    filterset_class = StudentCompletionFilter


