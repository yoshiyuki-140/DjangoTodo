from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'general/topPage.html')