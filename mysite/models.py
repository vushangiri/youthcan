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

class Team(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    post = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='pics')
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.first_name

class Partners(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name


