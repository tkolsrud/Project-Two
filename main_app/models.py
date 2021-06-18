from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField
from django.contrib.auth.models import User

import time
from time import strftime


# Create your models here.
class Post(Model):

    title = CharField(max_length=100)
    city = CharField(max_length=100)
    body = TextField(max_length=500)
    img = CharField(max_length=1000)
    create_at = DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_at']


# Extending User model
# Working to extend User model so we have more fields that update into database

class UserProfile(Model):
    # On delete CASCADE deletes all user info when user is deleted
    # Adding user to this like a foreign

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    current_city = models.CharField(max_length=400)
    user_img = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username
