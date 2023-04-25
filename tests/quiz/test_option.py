from rest_framework import status
from tests.test_fixtures import QuizTestSetup


class OptionTestCase(QuizTestSetup):

    def test_moder_list(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/option/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moder_create(self):
        self.client.force_authenticate(user=self.moder_user)
        bad_title_response = self.client.post(
            '/api/option/',
            {'question_1': 1, 'title': 'option_1', 'is_right': False})
        bad_is_right_response = self.client.post(
            '/api/option/',
            {'question_1': 1, 'title': 'option_1', 'is_right': True})
        response = self.client.post('/api/option/',
                                    {"question": 2, "title": "option"})
        self.assertEqual(bad_title_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(bad_is_right_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_moder_retrieve(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/option/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 1, 'title': 'option_1', 'is_right': False, 'question': 1})

    def test_moder_update(self):
        self.client.force_authenticate(user=self.moder_user)
        bad_is_right_response = self.client.put(
            '/api/option/1/',
            {'title': 'option_1', 'is_right': True, 'question': 1})
        bad_title_response = self.client.put(
            '/api/option/1/',
            {'title': 'option_2', 'is_right': False, 'question': 1})
        response = self.client.put(
            '/api/option/3/',
            {'title': 'option_3', 'is_right': True, 'question': 2})
        self.assertEqual(bad_is_right_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(bad_title_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moder_destroy(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.delete('/api/option/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_stud_list(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/option/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_stud_retrieve(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/option/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_stud_destroy(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/option/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anon(self):
        response_list = self.client.get('/api/option/')
        response_retrieve = self.client.get('/api/option/1/')
        response_destroy = self.client.delete('/api/option/1/')
        self.assertEqual(response_list.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_retrieve.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_destroy.status_code, status.HTTP_401_UNAUTHORIZED)
