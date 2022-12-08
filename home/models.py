from distutils.command.upload import upload
from django.db import models

# Create your models here

class Information(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to ='photo')
    description = models.TextField()