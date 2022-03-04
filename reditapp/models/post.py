from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from reditapp.models import Registration, UserProfile
from datetime import datetime


class Post(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    myprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    mypost = models.TextField(blank=True)
    postimage = models.ImageField(
        upload_to="uploadpost/", blank=True, null=True)
    postfile = models.FileField(upload_to="uploadfile/", blank=True, null=True)
    likes = models.ManyToManyField(Registration, related_name="post_likes")
    views = models.ManyToManyField(Registration, related_name="post_views")

    def total_likes(self):
        return self.likes.count()

    def total_views(self):
        return self.views.count()
