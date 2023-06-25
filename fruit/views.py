from django.shortcuts import render, redirect
from Fruitipedia.fruit.forms import ProfileCreateForm, FruitCreateFrom, FruitEditFrom, FruitDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from .models import Fruit
from .templatetags.custom_tags import get_profile


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruit = Fruit.objects.all()
    context = {
        'fruit': fruit,
    }
    return render(request, 'common/dashboard.html', context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    fruit = Fruit.objects.count()

    context = {
        'profile': profile,
        'fruit': fruit
    }

    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    fruit = Fruit.objects.all()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        for i in fruit:
            fruit_form = FruitDeleteForm(request.POST, instance=i)
            fruit_form.save()

        return redirect('index')

    context = {
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)


def fruit_create(request):
    form = FruitCreateFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    context = {
        'fruit': fruit
    }
    return render(request, 'fruit/details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitEditFrom(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit
    }
    return render(request, 'fruit/edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitDeleteForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
        'fruit': fruit
    }
    return render(request, 'fruit/delete-fruit.html', context)
