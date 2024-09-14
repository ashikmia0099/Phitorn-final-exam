
from django.urls import path
from .views import RegisterPage,LoginPage,LogoutView, activate

urlpatterns = [
    
    path('Register',RegisterPage, name='RegisterPage'),
    path('Login/',LoginPage, name='LoginPage'),
    path('Logout/',LogoutView, name='Logout'),
    path('active/<uid64>/<token>/',activate, name='activate')


]
