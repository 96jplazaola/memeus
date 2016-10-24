from django.db import models


class Memea(models.Model):
    izenburua = models.CharField(max_length=100)
    argazkia = models.CharField(max_length=200)
    datsegitKop = models.IntegerField(default=0)

    def __str__(self):
        return self.izenburua
