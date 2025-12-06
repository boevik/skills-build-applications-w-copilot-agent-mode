from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400)
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=500)
        Activity.objects.create(user=users[3], type='Yoga', duration=50, calories=200)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', description='Strength and flexibility', difficulty='Medium')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=600)


        # Ensure unique index on email for users using PyMongo
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
