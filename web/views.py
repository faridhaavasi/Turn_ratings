from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Turn, Mont
import ghasedakpack
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

        sms = ghasedakpack.Ghasedak("1fca2d5c8598fb09f04ab70c1e6c8eb4b399cccc335b696ef4e0cb3c59b644fb")
        masage = f'شماره{number}با مشخصات:{year}-{mont}در{day}و ساعت {hour} برای شما با شکاره پرونده{request.user.file_number} ثبت شد'
        sms.send({'message': masage, 'receptor': f'{request.user.phone_number}', 'linenumber': '3000xxxxx'})


        Turn.objects.get(id=id).delete()
        return redirect('web:home')


