from django.shortcuts import render, redirect
from apps.core.models import (
    Intro, Service, ServiceOptions, Faq, FaqQuestions,
    ConnectSection, ConnectShortAnswers, GetInTouch,
    Contact, ContactLinks
)
# Create your views here.
def home(request):
    
    #========================Intro===============================
    
    
    #=======================Get In Touch=========================
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        GetInTouch.objects.create(name=name, email=email, message=message)
        return redirect('home')
    
    context = {
        'intro' : Intro.objects.first(),
        'service' : Service.objects.first(),
        'service_options' : ServiceOptions.objects.all(),
        'faq' : Faq.objects.first(),
        'faq_questions' : FaqQuestions.objects.all(),
        'connect_section' : ConnectSection.objects.first(),
        'connect_short_answers' : ConnectShortAnswers.objects.all(),
        'contact' : Contact.objects.first(),
        'contact_links' : ContactLinks.objects.all(),
    }
    return render(request, 'index.html', context)