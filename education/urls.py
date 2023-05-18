from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path("education", views.EducationView.as_view(), name="education-page"),
]
