from django.urls import path
from websites import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name = "Home"),
    path('Clientes/', views.Clientes, name = "Clientes"),
]

