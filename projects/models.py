from django.db import models
from django.utils.text import slugify
from core.models import Profile
from skills.models import Skill
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="projects")
    url = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name="projects")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects", null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True,)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title.capitalize()
    
    def get_absolute_url(self):
        return reverse("project-detail-page", args=[self.slug])

class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=400)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="comments", null=True)
    
    def __str__(self):
        return self.text[:20]