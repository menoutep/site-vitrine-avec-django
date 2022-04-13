from django.contrib import admin
from .models import Message,Team, Portfolio, Images,Icone, Service
from django.contrib.auth.models import Group
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    search_fields=('title',)
    

class ServiceAdmin(admin.ModelAdmin):
    search_fields=('title','description')


class MessageAdmin(admin.ModelAdmin):
    search_fields=('subject', 'message')
    readonly_fields=["expediteur","subject","message","email"]

admin.site.unregister(Group)
admin.site.register(Images,ImageAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Team)
admin.site.register(Portfolio)
admin.site.register(Icone)

admin.site.site_header="My App Admistration"
