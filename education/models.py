from django.db import models

# Create your models here.

class Education(models.Model):
    instution = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    courses = models.TextField(max_length=500, null=True, default=None, blank=True)
    image = models.ImageField(upload_to="education", null=True, default=None, blank=True)
    description = models.TextField(max_length=500, null=True, default=None, blank=True)
    anticipated_graduation = models.BooleanField(default=False)

    def __str__(self):
        return self.instution