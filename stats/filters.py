from .models import Completion
from django_filters import rest_framework as filters


class CompletionFilter(filters.FilterSet):
    date = filters.DateRangeFilter(field_name='date')

    class Meta:
        model = Completion
        fields = {
            'user': ['exact'],
            'quiz': ['exact'],
            'category': ['exact'],
            'total': ['exact', 'gte', 'lte'],
            'rights': ['exact', 'gte', 'lte'],
            'max_score': ['exact', 'gte', 'lte'],
            'percent': ['exact', 'gte', 'lte'],
            'rate': ['exact', 'gte', 'lte'],
            'date': ['exact', 'gte', 'lte', 'gt', 'lt', 'range'],
        }


class StudentCompletionFilter(CompletionFilter):

    class Meta:
        model = Completion
        exclude = ('user', )  #student can only view his own stats

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)
