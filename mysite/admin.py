from django.contrib import admin
from .models import Contact, Newsletter, Team, Events, Eventsgallery, Whoarewe, Whatwedo, About, Values, Partners, Whoareweimage, Admin, Home, Advisors

# Register your models here.
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Team)

admin.site.register(Whatwedo)
admin.site.register(About)
admin.site.register(Values)
admin.site.register(Partners)
admin.site.register(Advisors)
admin.site.register(Admin)

admin.site.register(Home)

class EventsgalleryAdmin(admin.StackedInline):
    model = Eventsgallery

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    inlines = [EventsgalleryAdmin]

    class Meta:
       model = Events

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

@admin.register(Whoareweimage)
class WhoareweimageAdmin(admin.ModelAdmin):
    pass