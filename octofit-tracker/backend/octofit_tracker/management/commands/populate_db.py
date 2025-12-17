from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from djongo import models

from octofit_tracker import models as octofit_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        octofit_models.Activity.objects.all().delete()
        octofit_models.Workout.objects.all().delete()
        octofit_models.Team.objects.all().delete()
        octofit_models.Leaderboard.objects.all().delete()
        octofit_models.UserProfile.objects.all().delete()

        # Create teams
        marvel = octofit_models.Team.objects.create(name='Marvel')
        dc = octofit_models.Team.objects.create(name='DC')

        # Create users
        users = [
            {'email': 'ironman@marvel.com', 'name': 'Iron Man', 'team': marvel},
            {'email': 'spiderman@marvel.com', 'name': 'Spider-Man', 'team': marvel},
            {'email': 'batman@dc.com', 'name': 'Batman', 'team': dc},
            {'email': 'wonderwoman@dc.com', 'name': 'Wonder Woman', 'team': dc},
        ]
        user_objs = []
        for u in users:
            user = octofit_models.UserProfile.objects.create(email=u['email'], name=u['name'], team=u['team'])
            user_objs.append(user)

        # Create activities
        for user in user_objs:
            for i in range(3):
                octofit_models.Activity.objects.create(user=user, type='run', duration=30+i*5, distance=5+i, calories=200+i*10)

        # Create workouts
        for user in user_objs:
            octofit_models.Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session', duration=45)

        # Create leaderboard
        for team in [marvel, dc]:
            octofit_models.Leaderboard.objects.create(team=team, points=100 if team.name=='Marvel' else 80)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
