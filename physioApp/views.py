from django.shortcuts import render
from . models import *
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
      'programmes': Programme.objects.all(),
      'practicienes': Praticiene.objects.all(),
      'testimonials': Testimonial.objects.all(),
    }

    if request.method == "POST":
        contact = Message()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone_number = phone_number
        contact.subject = subject
        contact.message =  message
        contact.save()
        messages.success(request, f'{name} , attendez une réponse de ma part .')
        
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def physiothérapie(request):
    return render(request, 'pages/physiothérapie.html',)

def bienetre(request):
    return render(request, 'pages/bienetre.html',)


def price(request):
    context = { 
    'programmes': Programme.objects.all()
    }
    return render(request, 'pages/price.html', context)

def team(request):
    context = {
      'practicienes': Praticiene.objects.all(),
    }
    return render(request, 'pages/team.html', context)

def testimonials(request):
    context = {
        'testimonials': Testimonial.objects.all(),
    }
    return render(request, 'pages/testimonials.html', context)

def contact(request):
    
    if request.method == "POST":
        contact = Message()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone_number = phone_number
        contact.subject = subject
        contact.message =  message
        contact.save()
        messages.success(request, f'{name} , attendez une réponse de ma part .')

    return render(request, 'pages/contact.html',)

def appointment(request):
    return render(request, 'pages/appointment.html')

def machines(request):
    return render(request, 'pages/machines.html' )