# -*- coding: utf-8 -*-
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

    def test_fail_authentication(self):
        pass

    def test_successful_authentication(self):
        pass