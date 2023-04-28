from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import Login_form, Register_form, Check_otp_form
from random import randint
from .models import Otp, User
class User_login(View):
    def get(self, request):
        form = Login_form()
        return render(request, 'account/login.html', {'form': form})
    def post(self, request):
        form = Login_form(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone_number', "اطلاعات صحیح نیست")
        else:
            form.add_error('phone_number', "طلاعات صحیح نیست")
        return render(request, 'account/login.html', {'form': form})
class Register_user_lelel_1(View):
    def get(self, request):
        form = Register_form()
        return render(request, 'account/Register_l_1.html', {'form': form})
    def post(self, request):
        form = Register_form(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            code = randint(1000, 9999)
            print(code)
            Otp.objects.create(phone=cd['phone_number'], code=code)
            return redirect(reverse('account:check_otp') + f'?phone={cd["phone_number"]}')
        else:
            form.add_error('phone_number', "طلاعات صحیح نیست")
        return render(request, 'account/Register_l_1.html', {'form': form})

class Check_otp(View):
    def get(self, request):
        form = Check_otp_form()
        return render(request, 'account/check_otp.html', {'form': form})
    def post(self, request):
        form = Check_otp_form(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code']).exists():
                user = User.objects.create(phone_number=request.GET.get('phone'))
                login(request, user)
                return redirect('/')
            return form.add_error('code', 'اطلاعات درست نیست')
        return render(request, 'account/check_otp.html', {'form': form})













