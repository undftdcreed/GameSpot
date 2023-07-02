from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Game
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

class GameList(TemplateView):
  template_name = "game_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["games"] = Game.objects.all()
    return context



games = [
  Game("Monopoly", "https://image.api.playstation.com/cdn/UP0001/CUSA01061_00/CtpS1pOJWwFORlVvtg3CzgFQ260od4RE.png", "A monopoly is an enterprise that is the only seller of a good or service. In the absence of government intervention, a monopoly is free to set any price it chooses and will usually set the price that yields the largest possible profit."),
]


