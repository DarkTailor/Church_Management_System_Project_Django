from faker import Faker
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
import random

User = get_user_model()
fake = Faker()
generated_usernames = set()

def generate_fake_member():
    username = fake.user_name()
    while username in generated_usernames:
        # Regenerate username until a unique one is found
        username = fake.user_name()
    
    generated_usernames.add(username)

    name = fake.first_name()
    surname = fake.last_name()
    category = random.choice(['Adult', 'Teen', 'Sunday school', 'Visitor'])
    birthday = fake.date_of_birth(minimum_age=12, maximum_age=80)
    email = fake.email()

    member = User.objects.create_user(
        username=username,
        password=fake.password(),
        name=name,
        surname=surname,
        category=category,
        birthday=birthday,
        email=email,
    )

    # Add the member to random groups (you may customize this based on your actual groups)
    groups = Group.objects.all()
    for _ in range(random.randint(0, 3)):
        member.groups.add(random.choice(groups))

    return member

class Command(BaseCommand):
    help = 'Populate the database with fake members.'

    def handle(self, *args, **options):
        # Create 400 fake members
        for _ in range(400):
            generate_fake_member()

        self.stdout.write(self.style.SUCCESS("Database populated with 400 fake members."))
