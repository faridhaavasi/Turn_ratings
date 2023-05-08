from django.urls import path
from . import views
app_name = 'web'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('setpassword', views.Set_pass.as_view(), name='setpassword'),
]
