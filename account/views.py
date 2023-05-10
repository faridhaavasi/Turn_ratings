from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login, logout
from .forms import Login_form, Register_form, Check_otp_form, Editinfo_form
from random import randint
from .models import Otp, User
from django.utils.crypto import get_random_string


class User_login(View):
    def get(self, request):
        form = Login_form()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = Login_form(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(User, username=cd['phone_number'], password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect('/')

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
            token = get_random_string(length=50)
            print(code)
            Otp.objects.create(phone=cd['phone_number'], code=code, token=token)
            return redirect(reverse('account:check_otp') + f'?token={token}')
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
                otp = Otp.objects.get(token=request.GET.get('token'))

                user = User(phone_number=otp.phone)
                user.set_password(cd['password'])
                user.save()
                if user is not None:
                    login(request, user)
                    otp.delete()
                    return redirect('account:Edit_info', pk=user.id)

                else:
                    return form.add_error('code', 'اطلاعات درست نیست')

        return render(request, 'account/check_otp.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')

class Editinfo(UpdateView):
    model = User
    fields = ['fullname', 'email', 'phone_number', 'file_number']
    #form_class = Editinfo_form
    
    success_url = '/'
