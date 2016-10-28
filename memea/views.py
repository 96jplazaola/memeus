from django.shortcuts import render, get_object_or_404
from .models import Memea
from django.views.generic.edit import CreateView, DeleteView, UpdateView


def index(request):
    meme_denak = Memea.objects.all()
    context = {
        'memeDenak': meme_denak
    }
    return render(request, 'memea/index.html', context)


def details(request, meme_id):
    memea = get_object_or_404(Memea, pk=meme_id)
    return render(request, 'memea/details.html', {'memea': memea})


class MemeaSortu(CreateView):
    model = Memea
    fields = ['izenburua', 'argazkia']
