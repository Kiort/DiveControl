import factory
from factory.django import DjangoModelFactory

from diveapp.models import *

class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Locacija

        naziv = factory.Faker("sentence", nb_words=10)
        coordinate = factory.Faker("geo_coordinate")
        stvoreno = factory.Faker("date_time")