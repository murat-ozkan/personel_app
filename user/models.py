from django.db import models
from django.contrib.auth.models import User

class Profile(User, models.Model):
    image = models.CharField(max_length=700, null=True, blank=True)
    about =models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username