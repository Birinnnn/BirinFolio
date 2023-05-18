from django.views.generic import ListView, DetailView
from projects.models import Project
from django.shortcuts import redirect, get_object_or_404
from projects.forms import CommentForm
from django.contrib import messages

# Create your views here.

class ProjectsView(ListView):
    template_name = "projects/all-projects.html"
    model = Project
    ordering = ["-id"]
    context_object_name = "projects"

class ProjectDetailView(DetailView):
    template_name = "projects/project-detail.html"
    model = Project
    context_object_name = "project"

    def post(self, request, slug):
        project = get_object_or_404(Project, slug=slug)
        user = self.request.user
        if user.is_authenticated:
            if "submit_comment" in request.POST:
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.project = project
                    comment.user = user
                    comment.save()
                    return redirect("projects:project-detail-page", slug=project.slug)
            elif "like" in request.POST:
                if user in project.likes.all():
                    # User already liked the project
                    project.likes.remove(user)
                else:
                    # User has not liked the project yet
                    project.likes.add(user)
        else:
            # User is not logged in and tried to like
            if "like" in request.POST:
                messages.error(request, "You need to be logged in to like a project.")

        return redirect('projects:project-detail-page', slug=project.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = context["project"]
        context["tags"] = project.skills.all()
        context["comments"] = project.comments.order_by("-id")
        context["comment_form"] = CommentForm()
        context["liked"] = self.request.user.is_authenticated and project.likes.filter(pk=self.request.user.pk).exists()
        return context
