from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    overview = models.TextField()
    image = CloudinaryField('images')
