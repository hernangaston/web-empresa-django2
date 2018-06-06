from django.contrib import admin

from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')#puede ser lista o tupla

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name='Personal').exists():
			return ('key', 'name')
		else:
			return ('created', 'updated')


#adjuntamos la clase Service y su config ServiceAdmin
admin.site.register(Link, LinkAdmin)