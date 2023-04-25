from rest_framework import status
from tests.test_fixtures import QuizTestSetup


class CompletionTestCase(QuizTestSetup):
    def test_moder_list_retrieve(self):
        self.client.force_authenticate(user=self.moder_user)
        retrieve_response = self.client.get('/api/completions/moderator/1/')
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        list_response = self.client.get('/api/completions/moderator/')
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(list_response.json()['count'], 2)
        stats_response = self.client.get('/api/completions/moderator/stats/')
        self.assertEqual(stats_response.status_code, status.HTTP_200_OK)
        self.assertEqual(stats_response.json()['completions_quantity'], 2)

    def test_moder_create_update_destroy(self):
        self.client.force_authenticate(user=self.moder_user)
        create_response = self.client.post('/api/completions/moderator/',
                                           {'user': 2,
                                            'quiz': 1,
                                            'category': 1,
                                            'total': 2,
                                            'rights': 2,
                                            'max_score': 5,
                                            'percent': 100,
                                            'rate': 5})
        self.assertEqual(create_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        update_response = self.client.put('/api/completions/moderator/1/',
                                          {'user': 2,
                                           'quiz': 1,
                                           'category': 1,
                                           'total': 2,
                                           'rights': 0,
                                           'max_score': 5,
                                           'percent': 100,
                                           'rate': 5})
        self.assertEqual(update_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        destroy_response = self.client.delete('/api/completions/moderator/1/')
        self.assertEqual(destroy_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_stud_list_retrieve(self):
        self.client.force_authenticate(user=self.stud_user)
        retrieve_response = self.client.get('/api/completions/student/1/')
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        list_response = self.client.get('/api/completions/student/')
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(list_response.json()['count'], 1)
        user_filter_response = self.client.get('/api/completions/student/?user=3/')
        self.assertEqual(user_filter_response.json()['results'][0]['user'], 2)
        stats_response = self.client.get('/api/completions/student/stats/')
        self.assertEqual(stats_response.status_code, status.HTTP_200_OK)
        self.assertEqual(stats_response.json()['avg_rights_percent'], 100)


    def test_stud_create_update_destroy(self):
        self.client.force_authenticate(user=self.stud_user)
        create_response = self.client.post('/api/completions/student/',
                                           {'user': 2,
                                            'quiz': 1,
                                            'category': 1,
                                            'total': 2,
                                            'rights': 2,
                                            'max_score': 5,
                                            'percent': 100,
                                            'rate': 5}
                                           )
        self.assertEqual(create_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        update_response = self.client.put('/api/completions/student/1/',
                                          {'user': 2,
                                           'quiz': 1,
                                           'category': 1,
                                           'total': 2,
                                           'rights': 2,
                                           'max_score': 5,
                                           'percent': 1000,
                                           'rate': 5}
                                          )
        self.assertEqual(update_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        destroy_response = self.client.delete('/api/completions/student/1/')
        self.assertEqual(destroy_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_anon(self):
        moder_list_response = self.client.get('/api/completions/moderator/')
        moder_stats_response = self.client.get('/api/completions/moderator/stats/')
        moder_retrieve_response = self.client.get('/api/completions/moderator/1/')
        stud_list_response = self.client.get('/api/completions/student/')
        stud_stats_response = self.client.get('/api/completions/student/stats/')
        stud_retrieve_response = self.client.get('/api/completions/student/1/')
        self.assertEqual(moder_list_response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(moder_stats_response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(moder_retrieve_response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(stud_list_response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(stud_stats_response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(stud_retrieve_response.status_code, status.HTTP_401_UNAUTHORIZED)
