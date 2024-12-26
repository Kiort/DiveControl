import random

from django.db import transaction
from django.core.management.base import BaseCommand

from diveapp.models import Locacija
from diveapp.factory import (
    LocationFactory
)

NUM = 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Locacija]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM):
            author = LocationFactory()