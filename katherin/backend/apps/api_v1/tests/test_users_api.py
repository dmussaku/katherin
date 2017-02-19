# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase, APIClient


class TestPostUsersActivate(APITestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_non_authenticated_users_can_not_access_API(self):
        response = self.client.post('/api/v2/users/')

    def test_data_validation(self):
        pass

    def test_successful_password_setting(self):
        pass