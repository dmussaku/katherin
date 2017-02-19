# -*- coding: utf-8 -*-
import json

from rest_framework.test import APITestCase, APIClient

from apps.users.models import CustomUser


class TestPostAuthIndex(APITestCase):

    fixtures = ['users']

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_data_validation(self):
        self.assertEqual(CustomUser.objects.count(), 3)

    def test_invalid_data_submitted(self):
        response = self.client.post('/api/v1/auth/', follow=True)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, 
            {
                'errors': {
                    'email': ['This field is required.'], 
                    'password': ['This field is required.']
                    },
                'success': False
            }
            )

    def test_fail_authentication(self):
        response = self.client.post(
            '/api/v1/auth/',
            json.dumps({'email': 'amir@katherin.com', 'password': 'Random password'}),
            content_type='application/json',
            follow=True
            )
        self.assertEqual(response.status_code, 403)

    def test_successful_authentication(self):
        # Known fixtures password for all users 'qweasdzxc'
        response = self.client.post(
            '/api/v1/auth/',
            json.dumps({'email': 'amir@katherin.com', 'password': 'qweasdzxc'}),
            content_type='application/json',
            follow=True
            )
        self.assertEqual(response.status_code, 200)
