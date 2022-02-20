from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from reditapp.models import Registration, UserProfile, Post
from datetime import datetime


class Comment(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user.name + ": " + self.text[:15]
