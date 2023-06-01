from django.urls import path
from . import views
app_name = 'web'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('Turnlist', views.TurnList.as_view(), name='TurnList'),
    path('Turnlit/?<str:mont>', views.TurnList.as_view(), name='TurnList'),


]
