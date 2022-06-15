from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('add/', views.Add_task, name='add'),
    path('remove/', views.removeTask, name='remove'),
    path('Login/', views.Login, name='login'),
    path('Logout/', views.Logout, name='logout'),
]
