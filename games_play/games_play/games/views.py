from django.shortcuts import render, redirect

from games_play.games.forms import ProfileForm, GameForm, DeleteGameForm, DeleteProfileForm
from games_play.games.models import Profile, Game


def get_profile():
    return Profile.objects.first()


def home(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context=context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context=context)


def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GameForm()
    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context=context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games
    }
    return render(request, 'dashboard.html', context=context)


def details_game(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }
    return render(request, 'details-game.html', context=context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'edit-game.html', context=context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'delete-game.html', context=context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    all_games = games.count()
    if all_games > 0:
        average_rating = sum(game.rating for game in games) / all_games
    else:
        average_rating = 0
    context = {
        'profile': profile,
        'games': games,
        'all_games': all_games,
        'average_rating': average_rating,
    }
    return render(request, 'details-profile.html', context=context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'game': profile,
    }
    return render(request, 'delete-profile.html', context=context)