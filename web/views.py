from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Turn

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'web/index.html', {})

class TurnList(View):
    def get(self, request):
        turn = Turn.objects.all()
        return render(request, 'web/list_turn.html', context={'turn': turn})

class Save_Turn(View):
    def get(self, request):
        turn = Turn.objects.all()
        return render(request, 'web/list_turn.html', context={'turn': turn})
    def post(self, request):
        print(request.POST['mont'])
        if request.POST['mont']:
            return redirect('web:home')
        return redirect('web:TurnList')


