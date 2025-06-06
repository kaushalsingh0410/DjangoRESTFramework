from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]
    search_fields = ('name','std')
    list_filter = ('age',)
    ordering = ('id',)
    list_per_page = 5



admin.site.register(Student,StudentAdmin)
