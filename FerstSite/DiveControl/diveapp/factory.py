import factory
from factory.django import DjangoModelFactory
from diveapp.models import *
from datetime import datetime



class VlasnikClubFactory(DjangoModelFactory):
    class Meta:
        model = VlasnikClub

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    oib = factory.Faker("random_int", min=1000000000, max=9999999999)
    stvoreno = factory.Faker("date_time_this_century")


class DiveClubFactory(DjangoModelFactory):
    class Meta:
        model = DiveClub

    naziv = factory.Faker("company")
    maticni_broj  = factory.Faker("random_int", min=1000000000, max=9999999999)
    vlasnik = factory.SubFactory(VlasnikClubFactory)
    stvoreno = factory.Faker("date_time_this_century")


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Locacija

    naziv = factory.Faker("sentence", nb_words=10)
    coordinate = factory.Faker("random_int", min=1000, max=9999)
    stvoreno = factory.Faker("date_time_this_century")
    divclub = factory.SubFactory(DiveClubFactory)  # Using SubFactory to directly associate a DiveClub

