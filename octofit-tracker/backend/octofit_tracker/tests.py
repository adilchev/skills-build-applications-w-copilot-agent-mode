from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class APISmokeTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('teams', response.data)
        self.assertIn('users', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboard', response.data)
