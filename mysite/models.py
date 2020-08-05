from django.db import models

class ActiveModel(models.Model):
    active = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.active:
            # select all other active items
            qs = type(self).objects.filter(active=True)
            # except self (if self already exists)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            # and deactive them
            qs.update(active=False) 

        super(ActiveModel, self).save(*args, **kwargs)

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
        
class Admin(ActiveModel):
    facebook = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()
    linkedin = models.URLField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        
        return 'Personal data(only one)'
    class Meta:
        verbose_name_plural = 'Admin'

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

class Advisors(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    post = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Advisors'

class Partners(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='logo')
    url = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Partners'

class Events(models.Model):
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='events', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Events'
    
class Eventsgallery(models.Model):
    events = models.ForeignKey(Events, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='events', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Eventgallaries'

    def __str__(self):
        return self.events.title


class Whoarewe(ActiveModel):
    
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Whoarewe'

class Whoareweimage(models.Model):
    events = models.ForeignKey(Whoarewe, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='whoarewe', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Whoareweimage'

    def __str__(self):
        return self.events.title

class Values(ActiveModel):
    photo_small = models.ImageField(upload_to='values', blank=True, null=True)
    photo_big = models.ImageField(upload_to='values', blank=True, null=True)
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Values'

class Whatwedo(models.Model):
    photo = models.ImageField(upload_to='whatwedo', blank=True, null=True)
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Whatwedo'

class About(ActiveModel):
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'About'

class Home(ActiveModel):
    title = models.CharField(max_length=50)
    body = models.TextField()
    video_url = models.URLField()
    phone = models.BigIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Home'

