from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login ,name='login'),
    path('sign/', views.sign, name='sign'),
    path('ai/', views.ai, name='ai'),
    path('train-ai/', views.train_ai, name='train_ai'),
    path('retrieve-data/', views.retrieve_data, name='retrieve_data'),

]


