from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status
from tests.test_fixtures import QuizTestSetup
from quiz.views import AnswerStudentViewSet
from quiz.service import check_quiz


class CheckQuizTestCase(QuizTestSetup):
    def test_check_quiz(self):
        result_1 = check_quiz([self.answer_1, self.answer_2])
        self.assertEqual(
            result_1,
            {'quiz': self.quiz_2,
             'category': self.category_2,
             'total': 2,
             'rights': 2,
             'max_score': 5,
             'percent': 100,
             'rate': 5})
        result_2 = check_quiz([self.answer_1, self.answer_3])
        self.assertEqual(
            result_2,
            {'quiz': self.quiz_2,
             'category': self.category_2,
             'total': 2,
             'rights': 1,
             'max_score': 5,
             'percent': 50,
             'rate': 2})

    def test_answer_view(self):
        factory = APIRequestFactory()
        request = factory.post('/student/answer/',
                               [
                                   {
                                       "user": 2,
                                       "option": 6
                                   },
                                   {
                                       "user": 2,
                                       "option": 9
                                   }
                               ])
        view = AnswerStudentViewSet.as_view({'post': 'create'})
        force_authenticate(request, user=self.stud_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        request = factory.post('/student/answer/', [])
        force_authenticate(request, user=self.stud_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



