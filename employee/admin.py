from django.contrib import admin

from .models import Employee

class EmplyessAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]

admin.site.register(Employee,EmplyessAdmin)