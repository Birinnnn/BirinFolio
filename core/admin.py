from django.contrib import admin
from .models import Profile, SocialLink, AboutMe

# Register your models here.

admin.site.register(Profile)
admin.site.register(SocialLink)
admin.site.register(AboutMe)
