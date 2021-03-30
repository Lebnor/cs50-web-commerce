from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin
import uuid

class User(AbstractUser):
    pass

class Listing(models.Model):
    uuid = models.UUIDField(primary_key=False, editable=False, default = uuid.uuid4)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    photourl = models.CharField(max_length=150, blank=True)
    last_bid = models.IntegerField(blank=True, default=0)
    highest_bid = models.IntegerField(null=True, blank=True, default=0)
    highest_bidder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.IntegerField(blank=True, null=True, default=0)
    winner = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='won', null=True, blank=True, unique=False)
    following = models.ManyToManyField(User, related_name='following', blank=True, null=True)
    category = models.CharField(null=True, blank=True, max_length=32)
    owner = models.ForeignKey(User, null=True, blank=True, related_name='created', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    text = models.TextField(max_length=200, blank=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, blank=True)
    listing = models.ForeignKey(Listing, related_name='comments', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{self.text}"