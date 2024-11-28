from django.db import models
from django.utils import timezone



class VlasnikClub(models.Model):
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=50)
    oib = models.CharField(max_length=10)
    



class DiveClub(models.Model):
    naziv = models.CharField(max_length=30)
    maticni_broj = models.CharField(max_length=10)
    vlasnik = models.OneToOneField(
        VlasnikClub,
        on_delete=models.CASCADE,
    )



class Diver(models.Model):
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=50)
    oib = models.CharField(max_length=10)
    clanstvo = models.ManyToManyField(DiveClub)




class DC(models.Model):
    naziv = models.CharField(max_length=30)
    maticni_broj = models.CharField(max_length=10)
    adresa = models.CharField(max_length=100)


class Locacija(models.Model):
    naziv = models.CharField(max_length=25)
    coordinate = models.CharField(max_length=100)
    clanstvo = models.ManyToManyField(DC)