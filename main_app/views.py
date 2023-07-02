from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Game
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

# Create your views here.

class Home(TemplateView):
  template_name = "home.html"
    
class About(TemplateView):
  template_name = "about.html"

class Games:
  def __init__(self, name, image, bio):
    self.name = name
    self.image = image
    self.bio = bio

class GameCreate(CreateView):
   model = Game
   fields = ['name', 'img', 'bio']
   template_name = "game_create.html"
   success_url = "/games/"

class GameList(TemplateView):
  template_name = "game_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get("name")
    if name != None:
        context["games"] = Game.objects.filter(name__icontains=name)
        context["header"] = f"searching for {name}"
    else:
        context["games"] = Game.objects.all()
        context["header"] = "Top Shelf Games"
    return context

class GameDetail(DetailView):
   model = Game
   template_name = "game_detail.html"

class GameUpdate(UpdateView):
   model = Game
   fields = ['name', 'img', 'bio']
   template_name = "game_update.html"
   success_url = "/gamelist/"

games = [
  Game("Monopoly", "https://image.api.playstation.com/cdn/UP0001/CUSA01061_00/CtpS1pOJWwFORlVvtg3CzgFQ260od4RE.png", "A monopoly is an enterprise that is the only seller of a good or service. In the absence of government intervention, a monopoly is free to set any price it chooses and will usually set the price that yields the largest possible profit."),
]

