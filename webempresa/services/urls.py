from django.urls import path

from . import views as services_views

#FICHERO PARTICULAR DE URLS DE CORE

urlpatterns = [
	path('', services_views.services, name="services"),
]
