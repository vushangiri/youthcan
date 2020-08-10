from django.core.mail import send_mail
from django.db import models
from datetime import datetime, date

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
    class Meta:
        verbose_name_plural = 'Query - Messages'
class Newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = 'Query - Subscribed'
        
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
        verbose_name_plural = 'Base - Personal Data'

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

    class Meta:
        verbose_name_plural = 'Base - Team'

class Advisors(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    post = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Base - Advisors'

class Partners(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='logo')
    url = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Base - Partners'

class UpcomingModel(models.Model):
    upcoming = models.BooleanField(default=False)

    class Meta:
        abstract = True

    
    def save(self, *args, **kwargs):
        qs = type(self).objects.all().update(upcoming=True)
        q = type(self).objects.filter(upcoming=True)
        if self.organized_at > date.today():
            self.upcoming = True
        else:
            self.upcoming = False
        for i in q:
            if i.organized_at > date.today():
                if self.pk != i.pk:
                    
                    q = q.exclude(pk=i.pk)
        
        q.update(upcoming=False) 
        super(UpcomingModel, self).save(*args, **kwargs)

class Events(UpcomingModel):
    title = models.CharField(max_length=50, blank=True, null=True, default='Untitled') 
    slogan = models.CharField(max_length=50, blank=True, null=True, default='Untitled') 
    body_left = models.TextField(blank=True, null=True)
    body_right = models.TextField(blank=True, null=True)
    body_center = models.TextField(blank=True, null=True)
    body_quotes = models.TextField(blank=True, null=True)
    organized_at = models.DateField()
    brief_info = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='events', blank=True, null=True)
  

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Base - Events'
    

    
class Eventsgallery(models.Model):
    events = models.ForeignKey(Events, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='events', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Z: Do not open - Eventgallaries'

    def __str__(self):
        return self.events.title


class About(ActiveModel):
    body_first = models.TextField(blank=True, null=True)
    body_right = models.TextField(blank=True, null=True)
    body_left = models.TextField(blank=True, null=True)
    left_image = models.ImageField(upload_to='about')
    right_image = models.ImageField(upload_to='about')
    def __str__(self):
        return 'Create_only_one'
    
    class Meta:
        verbose_name_plural = 'About'

class AboutGallery(models.Model):
    data = models.ForeignKey(About, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='About', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Z: Do not open - Eventgallaries'

    def __str__(self):
        return 'Images'


class JoinUs(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    cv = models.FileField(upload_to='cv')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Query - JoinUs'

class HomeTitles(ActiveModel):
    home_our_work_span = models.CharField(max_length=200)
    home_our_work_head = models.CharField(max_length=200)
    home_third_section_span = models.CharField(max_length=200)
    home_third_section_head = models.CharField(max_length=200)
    about_our_work_span = models.CharField(max_length=200)
    about_our_work_head = models.CharField(max_length=200)
    about_image_gallery = models.CharField(max_length=200)
    events_our_work_span = models.CharField(max_length=200)
    events_our_work_head = models.CharField(max_length=200)
    all_our_team_span = models.CharField(max_length=200)
    all_our_team_head = models.CharField(max_length=200)
    all_our_advisors = models.CharField(max_length=200)
    all_our_partners = models.CharField(max_length=200)
    
    
    def __str__(self):
        return 'Title use only one'

    class Meta:
        verbose_name_plural = 'Base - Titles'


class Home(ActiveModel):
    body = models.TextField()
    video_url = models.URLField()


    def __str__(self):
        return 'Home use only one'

    class Meta:
        verbose_name_plural = 'Home - 1st'


class Whoarewe(ActiveModel):
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Create only one'
    
    class Meta:
        verbose_name_plural = 'Home - 2nd'


class Values(ActiveModel):
    photo_small = models.ImageField(upload_to='values', blank=True, null=True)
    photo_big = models.ImageField(upload_to='values', blank=True, null=True) 
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Values(Only one)'
    
    class Meta:
        verbose_name_plural = 'Home - 4th'


class Whoareweimage(models.Model):
    events = models.ForeignKey(Whoarewe, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='whoarewe', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Z: Do not open - Whoareweimage'

    def __str__(self):
        return 'images'
