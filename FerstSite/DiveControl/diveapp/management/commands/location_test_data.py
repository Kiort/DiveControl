import random

from django.db import transaction
from django.core.management.base import BaseCommand

from diveapp.models import *
from diveapp.factory import (
    LocationFactory,
    VlasnikClubFactory,
    DiveClubFactory
)

NUM = 10
NUMDK = 5
NUMVL = 5



class Command(BaseCommand): 
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Locacija, ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        
        
        for _ in range(NUMVL):
            vlasnik = VlasnikClubFactory() 
        
        for _ in range(NUMDK):
            club = DiveClubFactory()    
            
        for _ in range(NUM):
            lokacije = LocationFactory()