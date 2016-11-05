from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now


class Memea(models.Model):
    egilea = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,)
    izenburua = models.CharField(max_length=100)
    argazkia = models.ImageField()
    datsegitKop = models.IntegerField(default=0)
    ezdatsegitKop = models.IntegerField(default=0)
    igoData = models.DateTimeField(default=now)

    def get_absolute_url(self):
        return reverse('memea:index')

    def __str__(self):
        return self.izenburua


class MemePuntuazioa(models.Model):
    puntuazioa = models.IntegerField()
    puntuatzailea = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    memea = models.ForeignKey(Memea)


class MemeIruzkina(models.Model):
    iruzkina = models.CharField(max_length=300)
    iruzkintzailea = models.ForeignKey(User)
    memea = models.ForeignKey(Memea)
    data = models.DateTimeField(default=now)


class IruzkinPuntuazioa(models.Model):
    puntuazioa = models.IntegerField()
    puntuatzailea = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    iruzkina = models.ForeignKey(MemeIruzkina)

