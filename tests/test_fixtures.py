from rest_framework.test import APITestCase

from user.models import QuizAppUser
from quiz.models import QuizCategory, Quiz, Question, Option, Answer
from stats.models import Completion


class QuizTestSetup(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.moder_user = QuizAppUser.objects.create(
            username='moder_user', password='password', email='moder@test.com', is_moderator=True)
        cls.stud_user = QuizAppUser.objects.create(
            username='stud_user', password='password', email='stud@test.com', is_moderator=False)
        cls.stud_user_2 = QuizAppUser.objects.create(
            username='stud_user2', password='password', email='stud2@test.com', is_moderator=False)

        cls.category_1 = QuizCategory.objects.create(title='category_1')

        cls.quiz_1 = Quiz.objects.create(
            category=cls.category_1, creator=cls.moder_user, title='quiz_1', max_score=5, is_draft=False)

        cls.question_1 = Question.objects.create(
            quiz=cls.quiz_1, title='question_1', is_multi=False)
        cls.question_2 = Question.objects.create(
            quiz=cls.quiz_1, title='question_2', is_multi=True)

        cls.option_1 = Option.objects.create(
            question=cls.question_1, title='option_1', is_right=False)
        cls.option_2 = Option.objects.create(
            question=cls.question_1, title='option_2', is_right=True)

        cls.option_3 = Option.objects.create(
            question=cls.question_2, title='option_3', is_right=False)
        cls.option_4 = Option.objects.create(
            question=cls.question_2, title='option_4', is_right=True)
        cls.option_5 = Option.objects.create(
            question=cls.question_2, title='option_5', is_right=False)

        cls.category_2 = QuizCategory.objects.create(title='category_2')

        cls.quiz_2 = Quiz.objects.create(
            category=cls.category_2, creator=cls.moder_user, title='quiz_2', max_score=5, is_draft=True)

        cls.question_3 = Question.objects.create(
            quiz=cls.quiz_2, title='question_3', is_multi=False)

        cls.option_6 = Option.objects.create(
            question=cls.question_3, title='option_6', is_right=True)
        cls.option_7 = Option.objects.create(
            question=cls.question_3, title='option_7', is_right=False)

        cls.question_4 = Question.objects.create(
            quiz=cls.quiz_2, title='question_4', is_multi=True)

        cls.option_8 = Option.objects.create(
            question=cls.question_4, title='option_8', is_right=False)
        cls.option_9 = Option.objects.create(
            question=cls.question_4, title='option_9', is_right=True)
        cls.option_10 = Option.objects.create(
            question=cls.question_4, title='option_10', is_right=False)

        cls.answer_1 = Answer.objects.create(user=cls.stud_user, option=cls.option_6)
        cls.answer_2 = Answer.objects.create(user=cls.stud_user, option=cls.option_9)
        cls.answer_3 = Answer.objects.create(user=cls.stud_user, option=cls.option_8)

        cls.completion_1 = Completion.objects.create(
            user=cls.stud_user,
            quiz=cls.quiz_1,
            category=cls.category_1,
            total=2,
            rights=2,
            max_score=5,
            percent=100,
            rate=5
        )
        cls.completion_1 = Completion.objects.create(
            user=cls.stud_user_2,
            quiz=cls.quiz_2,
            category=cls.category_2,
            total=2,
            rights=2,
            max_score=5,
            percent=100,
            rate=5
        )

    def test_moder_list(self):
        pass

    def test_moder_create(self):
        pass

    def test_moder_retrieve(self):
        pass

    def test_moder_update(self):
        pass

    def test_moder_destroy(self):
        pass

    def test_stud_list(self):
        pass

    def test_stud_create(self):
        pass

    def test_stud_retrieve(self):
        pass

    def test_stud_update(self):
        pass

    def test_stud_destroy(self):
        pass

    def test_anon(self):
        pass
