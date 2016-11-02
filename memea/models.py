from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Memea(models.Model):
    egilea = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,)
    izenburua = models.CharField(max_length=100)
    argazkia = models.CharField(max_length=200)
    datsegitKop = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('memea:index')

    def __str__(self):
        return self.izenburua
