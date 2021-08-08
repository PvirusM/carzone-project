from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('contact/', views.contact, name = 'contact'),
]
