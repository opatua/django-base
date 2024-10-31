from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Example Seed"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.help)

        print("hello")
