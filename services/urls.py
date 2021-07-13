from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.index, name='index'),
    path('comp_repair/', views.comp, name='comp'),
    path('internet_services/', views.internet, name='internet'),
    path('screen_replacement/', views.screens, name='screens'),
    path('assign/', views.assign, name='assign')
]