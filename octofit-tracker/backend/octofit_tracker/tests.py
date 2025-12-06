from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, calories=300)
        self.workout = Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard')
        self.leaderboard = Leaderboard.objects.create(team=marvel, points=700)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.user.email, 'spiderman@marvel.com')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Hero HIIT')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.team.name, 'Marvel')
        self.assertEqual(self.leaderboard.points, 700)
