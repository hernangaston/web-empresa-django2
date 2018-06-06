from django.contrib import admin

from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')#puede ser lista o tupla
	list_display = ('title', 'order')

#adjuntamos la clase Service y su config ServiceAdmin
admin.site.register(Page, PageAdmin)