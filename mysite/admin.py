from django.contrib import admin
from .models import Contact, Newsletter, Team, Events, Eventsgallery, Whoarewe, About, Values, Partners, Whoareweimage, Admin, Home, Advisors, JoinUs, HomeTitles, AboutGallery
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.


admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Team)

class HomeTitlesAdmin(admin.ModelAdmin):
    class Media:
        
        js = ('assets/xtra/tiny.js',)
admin.site.register(HomeTitles, HomeTitlesAdmin)


class ValuesAdmin(admin.ModelAdmin):
    class Media:
        
        js = ('assets/xtra/tiny.js',)
admin.site.register(Values, ValuesAdmin)

admin.site.register(Partners)
admin.site.register(Advisors)
admin.site.register(Admin)
admin.site.register(JoinUs)

class HomeAdmin(admin.ModelAdmin):
    class Media:
        
        js = ('assets/xtra/tiny.js',)
admin.site.register(Home, HomeAdmin)

class EventsgalleryAdmin(admin.StackedInline):
    model = Eventsgallery

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    inlines = [EventsgalleryAdmin]

    class Meta:
       model = Events
    
    class Media:
        
        js = ('assets/xtra/tiny.js',)

@admin.register(Eventsgallery)
class EventsgalleryAdmin(admin.ModelAdmin):
    pass

class WhoareweimageAdmin(admin.StackedInline):
    model = Whoareweimage

@admin.register(Whoarewe)
class WhoareweAdmin(admin.ModelAdmin):
    inlines = [WhoareweimageAdmin]

    class Meta:
       model = Whoarewe
       
    class Media:
        
        js = ('assets/xtra/tiny.js',)

@admin.register(Whoareweimage)
class WhoareweimageAdmin(admin.ModelAdmin):
    pass


class AboutGalleryAdmin(admin.StackedInline):
    model = AboutGallery

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [AboutGalleryAdmin]

    class Meta:
       model = About
       
    class Media:
        
        js = ('assets/xtra/tiny.js',)

@admin.register(AboutGallery)
class AboutGalleryAdmin(admin.ModelAdmin):
    pass

