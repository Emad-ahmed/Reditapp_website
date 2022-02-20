from django.contrib import admin
from reditapp.models.registration import Registration
from reditapp.models.sharequestion import ShareFile
from reditapp.models.userprofile import UserProfile
from reditapp.models.post import Post
# Register your models here.


@admin.register(Registration)
class Registration(admin.ModelAdmin):
    list_display = ['id']


@admin.register(ShareFile)
class Registration(admin.ModelAdmin):
    list_display = ['id', 'departMent', 'subject_name', 'subject_code']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id']
