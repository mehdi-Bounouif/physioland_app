from django.contrib import admin
from . models import *
from django.contrib.auth.models import *
# Register your models here.

admin.site.site_header = 'Physioland Admin Panel'
admin.site.site_title = 'Physioland Admin Panel'
admin.site.index_title = "Welcome to Physioland Admin Panal"

class Contactadmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')
    list_filter = ('name','email')
    search_fields = ('name',)

admin.site.register(Message , Contactadmin)
admin.site.register(Testimonial )
admin.site.register(Praticiene )
admin.site.register(Programme )
admin.site.unregister(Group)


