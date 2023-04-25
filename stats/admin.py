from django.contrib import admin
from .models import Completion


@admin.register(Completion)
class CompletionAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'date', 'percent', 'rate')
    list_filter = ["user", "quiz"]
