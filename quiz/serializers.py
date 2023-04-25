from rest_framework import serializers
from .models import Quiz, QuizCategory, Question, Option, Answer


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        """
        Validation for adding more than one correct options to not multi question
        and for unique option title in question
        """
        question = data.get('question')
        is_multi = question.is_multi
        is_right = data.get('is_right')
        existing_right_options = Option.objects.filter(question=question, is_right=True)
        if not is_multi and is_right and existing_right_options.exists():
            raise serializers.ValidationError(
                'Adding more than one right option to not multi question', code=400)
        title = data.get('title')
        existing_option = Option.objects.filter(question=question, title=title).exclude(pk=self.instance.pk if self.instance else None).first()
        if existing_option:
            raise serializers.ValidationError(
                f'A option with the title "{title}" already exists in this question.', code=400)
        return data


class StudentOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        exclude = ('is_right',)


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

    def validate(self, data):
        """
        Validation for unique question title in quiz.
        """
        quiz = data.get('quiz')
        title = data.get('title')
        existing_question = Question.objects.filter(quiz=quiz, title=title).exclude(pk=self.instance.pk if self.instance else None).first()
        if existing_question:
            raise serializers.ValidationError(f'A question with the title "{title}" already exists in this quiz.')
        return data


class StudentQuestionSerializer(serializers.ModelSerializer):
    options = StudentOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ('creator',)


class StudentQuizSerializer(serializers.ModelSerializer):
    questions = StudentQuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = '__all__'


class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategory
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
