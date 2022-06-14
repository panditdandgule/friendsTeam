from django.shortcuts import render
from app1.models import New_Registration
# Create your views here.

def welcome_registration(request):
    return render(request, "welcome.html")


