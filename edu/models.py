from django.db import models


# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=30,)
    email = models.EmailField()
    text = models.TextField(max_length=250)
