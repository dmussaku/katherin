# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

from rest_framework.test import APITestCase, APIClient

from apps.users.models import Invite


class TestPostInvitesIndex(APITestCase):

    fixtures = ['users']

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_non_authenticated_users_can_not_access_API(self):
        response = self.client.post('/api/v1/invites/')
        self.assertEqual(response.status_code, 403)

    def test_invalid_data_submitted(self):
        client = APIClient()
        client.login(username='amir@katherin.com', password='qweasdzxc')
        response = client.post(
            '/api/v1/invites/',
            json.dumps({}),
            content_type='application/json',
            follow=True,
            )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data,
            {
                'errors': {
                    'authorization': ['This field is required.'],
                    'invitee_email': ['This field is required.']
                    },
                'success': False
            }
            )

    def test_invite_instance_successfully_created(self):
        client = APIClient()
        client.login(username='amir@katherin.com', password='qweasdzxc')

        # Test that before request there no Invite instances
        self.assertEqual(Invite.objects.count(), 0)
        response = client.post(
            '/api/v1/invites/',
            json.dumps({
                'invitee_email': 'newuser@email.com',
                'authorization': 1,
                'groups': [1, 2],
                'permissions': [1, 2]
                }),
            content_type='application/json',
            follow=True,
            )
        self.assertEqual(response.status_code, 200)
        # Test that after request one entry has been added
        self.assertEqual(Invite.objects.count(), 1)
        # Check that params have been properly saved
        invite = Invite.objects.first()
        self.assertEqual(invite.inviter.email, 'amir@katherin.com')
        self.assertEqual(invite.invitee_email, 'newuser@email.com')
        self.assertEqual(invite.authorization, 1)
        self.assertEqual(invite.groups, [1, 2])
        self.assertEqual(invite.permissions, [1, 2])
        self.assertIsNotNone(invite.token)
        self.assertEqual(
            invite.date_create.strftime('%Y%m%d'), 
            datetime.now().strftime('%Y%m%d')
            )
        self.assertEqual(
            invite.date_expire.strftime('%Y%m%d'), 
            (datetime.now() + timedelta(days=7)).strftime('%Y%m%d')
            )

