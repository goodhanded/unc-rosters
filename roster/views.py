from django.shortcuts import render
from roster.models import Team, Player
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, "home.html")

def team(request, pk):
    team = get_object_or_404(Team, id=pk)

    paginator = Paginator(team.player_set.all(), 10)
    page = request.GET.get('page')
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(paginator.num_pages)

    return render(request, "team.html", {'team': team, 'players': players})

def player(request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "player.html", {'player': player})
