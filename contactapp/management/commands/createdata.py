from lib2to3.pytree import Base
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        print("hello there")
        