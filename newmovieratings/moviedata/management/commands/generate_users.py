from django.core.management.base import BaseCommand
from moviedata.models import Rater
from django.contrib.auth.models import User


def generate_users():
    from faker import Faker
    fake = Faker()
    user_list = [x for x in {fake.user_name() for _ in range(9000)}]
    count = 0
    for rater in Rater.objects.all():
        if rater.user == None:
            rater.user = User.objects.create_user(user_list[count],password='password',email=fake.email())
            rater.save()
        count += 1

class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_users()
