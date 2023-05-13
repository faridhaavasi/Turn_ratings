from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Turn

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'web/index.html', {})

class TurnList(ListView):
    model = Turn
    template_name = 'web/list_turn.html'


