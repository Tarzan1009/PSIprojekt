from django.db import models
from projekt import settings
from django.contrib.auth.models import AbstractUser
from crum import get_current_user

class CustomUser(AbstractUser):
    pass
    PESEL = models.CharField(max_length=11)
    exclude = ['pracownik', ]

    def __str__(self):
        return self.username



class Klient(models.Model):
    PESEL = models.CharField(max_length=11)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    nrPrawaJazdy = models.CharField(max_length=16)
    created_by = models.ForeignKey('szkody.CustomUser', blank=True, null=True, default=None, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(Klient, self).save(*args, **kwargs)

    def __str__(self):
        return self.imie+' '+self.nazwisko


class Samochod(models.Model):

    nrRej = models.CharField(max_length=10)
    marka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    VIN = models.CharField(max_length=18)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    created_by = models.ForeignKey('szkody.CustomUser', blank=True, null=True, default=None, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(Samochod, self).save(*args, **kwargs)

    def __str__(self):
        return self.nrRej

class Zdarzenie(models.Model):
    adres = models.CharField(max_length=100)
    opis = models.CharField(max_length=200)
    created_by = models.ForeignKey('szkody.CustomUser', blank=True, null=True, default=None, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(Zdarzenie, self).save(*args, **kwargs)

    def __str__(self):
        return self.adres


class Uczestnicy(models.Model):

    SPRAWCA = 'S'
    POSZKODOWANY = 'P'
    ROLA_CHOICES = [
        (SPRAWCA, 'Sprawca'),
        (POSZKODOWANY, 'Poszkodowany'),
    ]
    rola = models.CharField(
        max_length=1,
        choices=ROLA_CHOICES,
        default=SPRAWCA,
    )
    samochod = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    zdarzenie = models.ForeignKey(Zdarzenie, on_delete=models.CASCADE)
    created_by = models.ForeignKey('szkody.CustomUser', blank=True, null=True, default=None, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(Uczestnicy, self).save(*args, **kwargs)