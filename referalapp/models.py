from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Refer(models.Model):
    referUser = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 254)

class Referal(models.Model):
    refer = models.ForeignKey(Refer, on_delete=models.CASCADE)