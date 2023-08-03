from django.shortcuts import render

def index(request):
    return render(request,'startups/index.html')

def startup(request):
    return render(request, 'startups/imagem.html')