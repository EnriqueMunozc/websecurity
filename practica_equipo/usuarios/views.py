from django.shortcuts import render

def home (request):
    return render(request, "home/index.html")

def dashboard (request):
    return render(request, "dashboard/dashboard.html")
