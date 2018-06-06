from django.urls import path

from . import views as contact_views

#FICHERO PARTICULAR DE URLS DE CORE

urlpatterns = [
	path('', contact_views.contact, name="contact"),
]
