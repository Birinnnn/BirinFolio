from django.shortcuts import render
from django.views.generic import ListView
from .models import Category
# Create your views here.

class SkillsView(ListView):
    template_name = "skills/skills.html"
    model = Category
    ordering = ["-id"]
    context_object_name = "categories"