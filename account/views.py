from django.shortcuts import render
from django.views.generic import View
from .forms import Login_form

class User_login(View):
    def get(self, request):
        form = Login_form()
        return render(request, 'account/login.html', {'form': form})
