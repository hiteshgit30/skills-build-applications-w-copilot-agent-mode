from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.user = User.objects.create(email="tony@stark.com", username="IronMan", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Upper body", difficulty="Easy")
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration_minutes=30, date="2025-12-14")
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100, rank=1)

    def test_api_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.data)

    def test_users_endpoint(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, 200)

    def test_activities_endpoint(self):
        response = self.client.get("/api/activities/")
        self.assertEqual(response.status_code, 200)

    def test_workouts_endpoint(self):
        response = self.client.get("/api/workouts/")
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_endpoint(self):
        response = self.client.get("/api/leaderboard/")
        self.assertEqual(response.status_code, 200)
