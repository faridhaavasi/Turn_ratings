from django.urls import path
from . import views
app_name = 'web'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('Turnlist', views.TurnList.as_view(), name='TurnList'),
    path('save_turn', views.Save_Turn.as_view(), name='save_turn'),

]
