from loremipsum import generate_paragraph, generate_sentence
from django.test import TestCase

from apps.realestate.models import City
from apps.users.models import CustomUser


class TestRealestate(TestCase):

    def setUp(self):
        admin = CustomUser.objects.create_superuser(
            email='admin@admin.com',
            first_name='Jack',
            last_name='Nicholson',
            password='123123123',
        )
        City.objects.create(
            name='Almaty',
            coordinates={
                'latitude': 43.222015,
                'longitude': 76.851248,
            },
            author=admin
        )

    def test_city_creation(self):
        almaty = City.objects.filter(name='Almaty').first()
        self.assertEqual(1, City.objects.count())
        self.assertEqual('Almaty', almaty.name)

        self.assertEqual(1, City.objects.filter(coordinates__latitude__gt=42).count())
        self.assertEqual(
            City.objects.count(),
            City.objects.filter(
                coordinates__latitude__gt=42,
                coordinates__longitude__lt=77
            ).count()
        )

        City.objects.create(
            name='New York',
            coordinates={
                'latitude': 40.712784,
                'longitude': -74.005941,
            },
            author=CustomUser.objects.first()
        )

        self.assertEqual(2, CustomUser.objects.count())
        self.assertEqual(2, City.objects.filter(coordinates__latitude__range=(39, 44)).count())
