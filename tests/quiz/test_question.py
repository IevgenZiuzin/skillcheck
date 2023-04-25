from rest_framework import status
from tests.test_fixtures import QuizTestSetup


class QuestionTestCase(QuizTestSetup):

    def test_moder_list(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/question/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moder_create(self):
        self.client.force_authenticate(user=self.moder_user)
        bad_title_response = self.client.post(
            '/api/question/',
            {'quiz': 1, 'title': 'question_1'})
        bad_quiz_response = self.client.post(
            '/api/question/',
            {'quiz': 3, 'title': 'question_3'})
        response = self.client.post(
            '/api/question/',
            {"quiz": 1, "title": "question"})
        self.assertEqual(bad_title_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(bad_quiz_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {'id': 5, 'quiz': 1, 'title': 'question', 'is_multi': False})

    def test_moder_retrieve(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/question/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 1, 'quiz': 1, 'title': 'question_1', 'is_multi': False})

    def test_moder_update(self):
        self.client.force_authenticate(user=self.moder_user)
        bad_title_response = self.client.put(
            '/api/question/1/',
            {'quiz': 1, 'title': 'question_2', 'is_multi': True})
        bad_quiz_response = self.client.put(
            '/api/question/1/',
            {'quiz': 3, 'title': 'question', 'is_multi': False})
        response = self.client.put(
            '/api/question/1/',
            {'quiz': 1, 'title': 'question_1', 'is_multi': True})
        self.assertEqual(bad_title_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(bad_quiz_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 1, 'quiz': 1, 'title': 'question_1', 'is_multi': True})

    def test_moder_destroy(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.delete('/api/question/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_stud_list(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/question/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_stud_retrieve(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/question/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_stud_destroy(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/question/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anon(self):
        response_list = self.client.get('/api/question/')
        response_retrieve = self.client.get('/api/question/1/')
        response_destroy = self.client.delete('/api/question/1/')
        self.assertEqual(response_list.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_retrieve.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_destroy.status_code, status.HTTP_401_UNAUTHORIZED)
