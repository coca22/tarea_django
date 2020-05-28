"""proyect_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from polls.views.homeView import homeView


urlpatterns = [
    path('', homeView.home, name='home'),
    path('formulario/', homeView.formulario, name='formulario'),
    path('formulario2/', homeView.formulario2, name='formulario2'),
    path('formulario3/', homeView.formulario3, name='formulario3'),
    path('formulario4/', homeView.formulario4, name='formulario4'),
    path('formulario5/', homeView.formulario5, name='formulario5')

]