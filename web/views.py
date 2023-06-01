from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Turn, Mont


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'web/index.html', {})


class TurnList(View):

    def get(self, request):

        mont = request.GET.get('mont', 'فروردین')
        monts = Mont.objects.all()
        turn = Turn.objects.filter(time__mont__name__icontains=mont)


        return render(request, 'web/list_turn.html', context={'turn': turn, 'monts': monts})


    def post(self, request):
        id = request.POST['id']
        number = request.POST['number']
        year = request.POST['year']
        mont = request.POST['mont']
        day = request.POST['day']
        hour = request.POST['hour']
        turn = Turn.objects.all()

        Turn.objects.get(id=id).delete()
        return redirect('web:home')


