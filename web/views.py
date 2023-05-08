from django.shortcuts import render, redirect
from django.views.generic import View, edit
from .forms import Set_Pass_Form
from account.models import User, Otp
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'web/index.html', {})

class Set_pass(View):
    def get(self, request):
        form = Set_Pass_Form()
        return render(request, 'web/setpassword.html', {'form': form})
    def post(self, request):
        form = Set_Pass_Form(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            password = cd['password']
            otp = Otp.objects.get(token=request.GET.get('token'))
            user = User.objects.get(phone_number=otp.phone)
            user.password = password
            return redirect('web:home')
        return render(request, 'web/setpassword.html', {'form': form})




