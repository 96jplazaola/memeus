from django.db import models
from django.core.urlresolvers import reverse


class Memea(models.Model):
    izenburua = models.CharField(max_length=100)
    argazkia = models.CharField(max_length=200)
    datsegitKop = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('memea:index')

    def __str__(self):
        return self.izenburua
