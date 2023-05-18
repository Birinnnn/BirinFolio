from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="skills")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return self.name
    