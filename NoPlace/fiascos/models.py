from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    updated_date = models.DateTimeField(auto_now=True)
