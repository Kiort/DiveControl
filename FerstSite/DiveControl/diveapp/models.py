from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class VlasnikClub(models.Model):
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=50)
    oib = models.CharField(max_length=10)
    stvoreno=models.DateTimeField(default=datetime.now)
    



class DiveClub(models.Model):
    naziv = models.CharField(max_length=30)
    maticni_broj = models.CharField(max_length=10)
    vlasnik = models.OneToOneField(
        VlasnikClub,
        on_delete=models.CASCADE,
    )
    stvoreno=models.DateTimeField(default=datetime.now)



class Diver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='diver', default=1)
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=50)
    oib = models.CharField(max_length=10)
    clanstvo = models.ManyToManyField(DiveClub)
    stvoreno=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.ime} {self.prezime}"

class Locacija(models.Model):
    naziv = models.CharField(max_length=25)
    coordinate = models.CharField(max_length=100)
    stvoreno=models.DateTimeField(default=datetime.now)
    divclub= models.ForeignKey(DiveClub, on_delete=models.CASCADE, default=None)