from django.contrib import admin
from .models import Memea, MemeIruzkina, IruzkinPuntuazioa, MemePuntuazioa


class MemeaModelAdmin(admin.ModelAdmin):
    list_display = ['izenburua', 'egilea', 'igoData']
    list_filter = ['igoData']
    search_fields = ['izenburua']

    class Meta:
        model = Memea

admin.site.register(Memea, MemeaModelAdmin)
admin.site.register(MemeIruzkina)
admin.site.register(IruzkinPuntuazioa)
admin.site.register(MemePuntuazioa)
