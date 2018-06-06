from django import template
from pages.models import Page

register = template.Library()
#registramos la template tag n la libreria de templates asi puede estar disponible en todas las templates
@register.simple_tag
def get_page_list():
	pages = Page.objects.all()
	return pages