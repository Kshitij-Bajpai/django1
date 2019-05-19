from django.shortcuts import render
# Create your views here.
from .models import Contact


def index(request):
    return render(request, 'mysite/index.html')

def contact(request):
    if request.method =="POST":
        email_r = request.POST.get('email')
        phone_r = request.POST.get('phone')
        message_r = request.POST.get('message')

        c = Contact(email = email_r, phone = phone_r, message = message_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/Contact.html')

def Portfolio(request):
    return render(request, 'mysite/portfolio.html')