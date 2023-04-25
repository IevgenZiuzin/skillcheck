from rest_framework import status
from tests.test_fixtures import QuizTestSetup


class CategoryTestCase(QuizTestSetup):

    def test_moder_list(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moder_retrieve(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.get('/api/category/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moder_destroy(self):
        self.client.force_authenticate(user=self.moder_user)
        response = self.client.delete('/api/category/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_stud_list(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stud_retrieve(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.get('/api/category/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stud_destroy(self):
        self.client.force_authenticate(user=self.stud_user)
        response = self.client.delete('/api/category/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_anon(self):
        response_list = self.client.get('/api/category/')
        response_retrieve = self.client.get('/api/category/1/')
        response_destroy = self.client.delete('/api/category/1/')
        self.assertEqual(response_list.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_retrieve.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_destroy.status_code, status.HTTP_401_UNAUTHORIZED)
