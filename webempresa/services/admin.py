from django.contrib import admin

from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')#puede ser lista o tupla

#adjuntamos la clase Service y su config ServiceAdmin
admin.site.register(Service, ServiceAdmin)