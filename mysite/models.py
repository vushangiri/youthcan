from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email