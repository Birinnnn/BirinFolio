from django.shortcuts import render
from django.views.generic import ListView
from .models import Education

# Create your views here.
class EducationView(ListView):
    template_name = "education/education.html"
    model = Education
    ordering = ["-id"]
    context_object_name = "educations"