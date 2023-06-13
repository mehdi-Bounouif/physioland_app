from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('physiothérapie', views.physiothérapie, name='physiothérapie'),
    path('bienetre', views.bienetre, name='bienetre'),
    path('price', views.price, name='price'),
    path('team', views.team, name='team'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('contact', views.contact, name='contact'),
    path('appointment', views.appointment, name='appointment'),
    path('machine', views.machines, name='machines'),
]