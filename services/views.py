from django.shortcuts import render
from services.models import Servicio 

# Create your views here.
def Servicios(request):
    servicios=Servicio.objects.all()
    return render(request, "servicios.html", {"servicios":servicios})