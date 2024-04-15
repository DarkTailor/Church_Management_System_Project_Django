import random
from faker import Faker
from django.core.management.base import BaseCommand
from Donations.models import Donations  # Make sure to import your Donations model

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake donations.'

    def handle(self, *args, **options):
        donation_types = ['T', 'OG']  # Define the possible donation types

        # Create 400 fake donations
        for _ in range(400):
            donation = Donations.objects.create(
                type=random.choice(donation_types),
                amount=random.uniform(1, 1000),  # Adjust the range based on your needs
                description=fake.text(),
            )

        self.stdout.write(self.style.SUCCESS("Database populated with 400 fake donations."))
