from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('login', views.User_login.as_view(), name='login'),
]