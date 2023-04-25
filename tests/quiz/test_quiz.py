from rest_framework import status
from tests.test_fixtures import QuizTestSetup


class QuizTestCase(QuizTestSetup):

    def test_moder_list(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/moderator/quiz/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moder_create(self):
        self.client.force_authenticate(user=self.moder_user)
        bad_category_response = self.client.post(
            '/api/moderator/quiz/',
            {'category': 3, 'title': 'quiz_3', 'max_score': 5})
        bad_title_response = self.client.post(
            '/api/moderator/quiz/',
            {'category': 1, 'title': 'quiz_1', 'max_score': 5})
        bad_max_score_response = self.client.post(
            '/api/moderator/quiz/',
            {'category': 1, 'title': 'quiz_3', 'max_score': 0})
        response = self.client.post(
            '/api/moderator/quiz/',
            {'category': 1, 'title': 'quiz_3', 'max_score': 5})
        self.assertEqual(bad_category_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(bad_title_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(bad_max_score_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(),
                         {'id': 3, 'category': 1, 'creator': 1, 'title': 'quiz_3', 'max_score': 5, 'is_draft': True})

    def test_moder_retrieve(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/moderator/quiz/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 1, 'category': 1, 'creator': 1, 'title': 'quiz_1', 'max_score': 5, 'is_draft': False})

    def test_moder_update(self):
        self.client.force_authenticate(user=self.moder_user)
        response_update = self.client.put('/api/moderator/quiz/1/',
                                          {'category': 1, 'title': 'quiz_3', 'max_score': 5, 'is_draft': False})
        response_partial_update = self.client.patch('/api/moderator/quiz/1/',
                                                    {'is_draft': True})
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_partial_update.status_code, status.HTTP_200_OK)

    def test_moder_destroy(self):
        self.client.force_authenticate(user=self.moder_user)
        response_delete = self.client.delete('/api/moderator/quiz/1/')
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_stud_list(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/student/quiz/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)

    def test_stud_retrieve(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/student/quiz/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['questions'][0]['options'][0]['title'], 'option_1')

    def test_stud_destroy(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.delete('/api/student/quiz/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_anon(self):
        response_student_list = self.client.get('/api/student/quiz/')
        response_student_retrieve = self.client.post('/api/student/quiz/1/')
        response_list = self.client.get('/api/moderator/quiz/')
        response_retrieve = self.client.get('/api/moderator/quiz/1/')
        response_destroy = self.client.delete('/api/moderator/quiz/1/')
        self.assertEqual(response_student_list.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_student_retrieve.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_list.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_retrieve.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_destroy.status_code, status.HTTP_401_UNAUTHORIZED)

