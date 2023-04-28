from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('login', views.User_login.as_view(), name='login'),
    path('register', views.Register_user_lelel_1.as_view(), name='register'),
    path('checkotp', views.Check_otp.as_view(), name='check_otp'),
]