from django.test import TestCase
from django.test.client import Client


class RHMTestCase(TestCase):

    def test_get_generate_hash(self):
        client = Client()
        response = client.get('/rhm/generate_hash/')

        self.assertEqual(response.status_code, 200)


    def test_get_check_hash(self):
        client = Client()

        response      = client.get('/rhm/check_hash/')
        response_data = response.json()

        if response_data[-1].isdigit() and int(response_data[-1]) % 2 == 0:
            self.assertEqual(response.status_code, 200)


    def test_load(self):
        for i in range(15):
            print(f'Running load test attempt {i+1}')
            self.test_get_check_hash()
