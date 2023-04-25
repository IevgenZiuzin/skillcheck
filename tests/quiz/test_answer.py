from rest_framework import status
from tests.test_fixtures import QuizTestSetup


class AnswerTestCase(QuizTestSetup):

    def test_moder_list(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/moderator/answer/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moder_create(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.post('/api/moderator/answer/', {'user': self.moder_user.id, 'option': 1})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_moder_retrieve(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/moderator/answer/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moder_update(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.put('/api/moderator/answer/1', {'user': self.moder_user.id, 'option': 2})
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_moder_destroy(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.delete('/api/moderator/answer/1')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_stud_list(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/student/answer/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_stud_create(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.post('/api/student/answer/', [{'user': self.stud_user.id, 'option': 1}])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_stud_retrieve(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/student/answer/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_stud_update(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.put('/api/student/answer/1', {'user': self.moder_user.id, 'option': 2})
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_stud_destroy(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.delete('/api/student/answer/1')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_anon(self):
        response_list = self.client.get('/api/student/answer')
        response_retrieve = self.client.get('/api/moderator/answer/1/')
        response_destroy = self.client.delete('/api/student/answer/1/')
        self.assertEqual(response_list.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        self.assertEqual(response_retrieve.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_destroy.status_code, status.HTTP_401_UNAUTHORIZED)
