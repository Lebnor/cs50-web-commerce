from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin
import uuid

class User(AbstractUser):
    pass

class Listing(models.Model):
    uuid = models.UUIDField(primary_key=False, editable=False, default = uuid.uuid4)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=100)
    photourl = models.CharField(max_length=150, blank=True)
    bid = models.IntegerField(blank=True)
    winner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, unique=False)
    following = models.ManyToManyField(User, related_name='following', blank=True, null=True)
    category = models.CharField(null=True, blank=True, max_length=32)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    text = models.TextField(max_length=200, blank=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, blank=True)
    listing = models.ForeignKey(Listing, related_name='comments', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{self.text}"