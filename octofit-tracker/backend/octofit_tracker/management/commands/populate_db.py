from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', username='IronMan', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', username='Batman', team=dc)
        clark = User.objects.create(email='clark@kent.com', username='Superman', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        squats = Workout.objects.create(name='Squats', description='Lower body', difficulty='Easy')

        # Create Activities
        Activity.objects.create(user=tony, activity_type='Pushups', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Running', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='Squats', duration_minutes=20, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Running', duration_minutes=60, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=120, rank=1)
        Leaderboard.objects.create(user=steve, points=110, rank=2)
        Leaderboard.objects.create(user=clark, points=100, rank=3)
        Leaderboard.objects.create(user=bruce, points=90, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
