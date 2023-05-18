from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path("skills", views.SkillsView.as_view(), name="skills-page"),
]
