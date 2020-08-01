from django.contrib import admin
from .models import Contact, Newsletter, Team

# Register your models here.
admin.site.register(Contact),
admin.site.register(Newsletter)
admin.site.register(Team)