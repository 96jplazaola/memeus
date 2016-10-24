from django.shortcuts import render, get_object_or_404
from .models import Memea


def index(request):
    meme_denak = Memea.objects.all()
    context = {
        'memeDenak': meme_denak
    }
    return render(request, 'memea/index.html', context)


def details(request, meme_id):
  '''

    try:
        memea = Memea.objects.get(pk=meme_id)
    except Memea.DoesNotExist:
        raise Http404("Meme hau ez da existitzen")
    Hau ein biharrian behekua eitten da
  '''
  memea = get_object_or_404(Memea,pk=meme_id)
    return render(request, 'memea/details.html', {'memea': memea})
