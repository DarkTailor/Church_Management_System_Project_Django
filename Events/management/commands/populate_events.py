import random
from faker import Faker
from django.core.management.base import BaseCommand
from Events.models import Events  # Make sure to import your Events model
from django.utils import timezone

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake events.'

    def handle(self, *args, **options):
        event_names = ['Event A', 'Event B', 'Event C']  # Define possible event names

        # Create 400 fake events
        for _ in range(400):
            event = Events.objects.create(
                Event=random.choice(event_names),
                Date=timezone.now() + timezone.timedelta(days=random.randint(1, 365)),  # Random date within the next year
                Time=fake.time(),
            )

        self.stdout.write(self.style.SUCCESS("Database populated with 400 fake events."))
