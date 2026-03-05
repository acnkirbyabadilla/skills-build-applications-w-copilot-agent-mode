from django.core.management.base import BaseCommand
from octofit_tracker import models
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User = get_user_model()
        models.Team.objects.all().delete()
        models.Activity.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        models.Workout.objects.all().delete()
        User.objects.all().delete()

        # Create Teams
        marvel = models.Team.objects.create(name='Marvel')
        dc = models.Team.objects.create(name='DC')

        # Create Users (superheroes)
        users = []
        users.append(User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel))
        users.append(User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel))
        users.append(User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc))
        users.append(User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc))

        # Create Activities
        for user in users:
            models.Activity.objects.create(user=user, type='run', duration=30)
            models.Activity.objects.create(user=user, type='cycle', duration=45)

        # Create Workouts
        for user in users:
            models.Workout.objects.create(user=user, name='Morning Routine', description='Pushups and Situps')

        # Create Leaderboard
        models.Leaderboard.objects.create(team=marvel, points=100)
        models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
