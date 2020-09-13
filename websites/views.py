from django.shortcuts import render, HttpResponse

def Home(request):
    return render(request, "home.html")

def Clientes(request):
    return render(request, "clientes.html")



# Create your views here.
