from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, related_name="profile")
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(
        upload_to="avatars", default="avatars/default.png")
    cv = models.FileField(upload_to="cvs", blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class SocialLink(models.Model):
    SOCIAL_CHOICES = (
        ('github', 'Github'),
        ('linkedin', 'Linkedin'),
        ('instagram', 'Instagram'),
        ('leetcode', 'Leetcode'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(
        max_length=15, choices=SOCIAL_CHOICES, default="other")

    def __str__(self):
        return self.name

class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="about_me")
    links = models.ManyToManyField(SocialLink, blank=True, related_name="about_me")

    def __str__(self):
        return self.title



