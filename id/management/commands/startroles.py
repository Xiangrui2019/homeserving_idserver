from django.core.management.base import BaseCommand
from id.models import UserRole


class Command(BaseCommand):
    def handle(self, *args, **options):
        default_roles = [
            "root",
            "administrator",
            "friend",
            "user"
        ]

        for role in default_roles:
            try:
                UserRole.objects.create(name=role)
                print("Created {0} role in database".format(role))
            except:
                print("Creating had an exception.")

        print("Created all roles.")
