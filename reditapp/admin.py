from django.contrib import admin
from reditapp.models.registration import Registration

# Register your models here.


@admin.register(Registration)
class Registration(admin.ModelAdmin):
    list_display = ['id']
