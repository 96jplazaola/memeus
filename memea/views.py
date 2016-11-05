from django.shortcuts import render, get_object_or_404
from .models import Memea
from django.contrib.auth import authenticate, login
from .forms import UserForm, MemeaForm
from django.contrib.auth.decorators import login_required


def index(request):
    meme_denak = Memea.objects.all()
    meme_denak = reversed(meme_denak)  # Azkenengo igo dan memia lehenengo egon deixen listan.
    context = {
        'memeDenak': meme_denak
    }
    return render(request, 'memea/index.html', context)


def details(request, meme_id):
    memea = get_object_or_404(Memea, pk=meme_id)
    context = {
        'memea': memea
    }
    return render(request, 'memea/details.html', context)


@login_required(login_url='/login/')
def memeasortu(request):
    form = MemeaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        memea = form.save(commit=False)
        memea.egilea = request.user
        memea.save()
        return index(request)

    context = {
        "form": form,
    }
    return render(request, 'memea/memea_form.html', context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return index(request)
    context = {
        "form": form,
    }
    return render(request, 'registration/registration.html', context)
