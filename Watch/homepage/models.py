from django.db import models

# Create your models here.
class watches(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField()

    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

class WatchesUpload(models.Model):
    name= models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='watch-image/')

    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)