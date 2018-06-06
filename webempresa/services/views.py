from django.shortcuts import render

from .models import Service

# Create your views here.
def services(request):
	services = Service.objects.all()
	title = "Servicios"
	d = dict(title=title, services=services)
	return render(request, "services/services.html", d)