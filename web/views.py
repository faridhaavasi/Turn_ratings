from django.shortcuts import render
from django.views.generic import View, edit
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'web/index.html', {})