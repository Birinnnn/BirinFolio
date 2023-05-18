from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path("projects", views.ProjectsView.as_view(), name="projects-page"),
    path("projects/<slug:slug>", views.ProjectDetailView.as_view(), name="project-detail-page"),
]
