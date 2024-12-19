from django.db import models
from django.utils import timezone



class VlasnikClub(models.Model):
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=50)
    oib = models.CharField(max_length=10)
    stvoreno=models.DateTimeField(auto_now_add=True)
    



class DiveClub(models.Model):
    naziv = models.CharField(max_length=30)
    maticni_broj = models.CharField(max_length=10)
    vlasnik = models.OneToOneField(
        VlasnikClub,
        on_delete=models.CASCADE,
    )
    stvoreno=models.DateTimeField(auto_now_add=True)



class Diver(models.Model):
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=50)
    oib = models.CharField(max_length=10)
    clanstvo = models.ManyToManyField(DiveClub)
    stvoreno=models.DateTimeField(auto_now_add=True)




class DC(models.Model):
    naziv = models.CharField(max_length=30)
    maticni_broj = models.CharField(max_length=10)
    adresa = models.CharField(max_length=100)
    stvoreno=models.DateTimeField(auto_now_add=True)


class Locacija(models.Model):
    naziv = models.CharField(max_length=25)
    coordinate = models.CharField(max_length=100)
    clanstvo = models.ManyToManyField(DC)
    stvoreno=models.DateTimeField(auto_now_add=True)