from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import Login_form

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
