from django.shortcuts import render
from .models import Feature

def home(request):
    features = Feature.objects.all()  # Fetch from DB
    return render(request, "home.html", {"features": features})
