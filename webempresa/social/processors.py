#creamos un procesador de contexto para extender el contexto de nuestras apps
#hay que agregarlo al achivo settings

from .models import Link

def ctx_dict(request):
	d = {}
	links = Link.objects.all()
	for link in links:
		d[link.key] = link.url
	return d