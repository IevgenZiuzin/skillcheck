from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import (
    QuizCategory, Quiz, Question, Option, Answer
)


class OptionInline(admin.TabularInline):
    model = Option


class QuestionInline(admin.TabularInline):
    model = Question
    inlines = [OptionInline]


class QuizInline(admin.TabularInline):
    model = Quiz


@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [QuizInline]


@admin.register(Quiz)
class Quiz(admin.ModelAdmin):
    list_display = ('title', 'category')
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'quiz')
    inlines = [OptionInline]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date')