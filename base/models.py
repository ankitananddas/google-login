from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.OneToOneField(
        User, related_name='email+', on_delete=models.CASCADE)


class Task(models.Model):
    descrip = models.TextField()
    title = models.CharField(max_length=40)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
