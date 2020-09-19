from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = ''
    return render(request, 'home.html', {'title': my_title})

def conditions_page(request):
    my_title = 'Conditions'
    return render(request, 'conditions.html', {'title': my_title})

def services_page(request):
    my_title = 'Services'
    return render(request, 'services.html', {'title': my_title})

def about_page(request):
    my_title = 'About Me'
    return render(request, 'about.html', {'title': my_title})

def FAQ_page(request):
    my_title = 'Frequently Asked Questions'
    return render(request, 'FAQ.html', {'title': my_title})

def contact_page(request):
    my_title = ''
    return render(request, 'contact.html', {'title': my_title})

def book_appointment_page(request):
    my_title = ''
    return render(request, 'book_appointment.html', {'title': my_title})

# def FAQ_page(request):
#     return HttpResponse('<h1>FAQQQQQQ</h1>')