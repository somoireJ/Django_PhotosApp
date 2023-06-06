from django.db import models
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title


class Portrait(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title


class Artwork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
