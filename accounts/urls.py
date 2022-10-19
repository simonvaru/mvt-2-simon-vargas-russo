from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.mi_login, name='login') 
]
