from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from core.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
# Create your views here.


class LoginView(SuccessMessageMixin, FormView):
    template_name = "core/login.html"
    form_class = LoginForm
    success_url = "core:home"
    success_message = "You logged in successfully!"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user is not None:
            login(self.request, user)
            return redirect('core:home')

        form.add_error(None, "Invalid username or password.")
        return self.form_invalid(form)


class LogoutView(SuccessMessageMixin, View):
    success_message = "You logged out successfully!"

    def get(self, request):
        logout(request)
        return redirect("core:login")


class RegisterView(SuccessMessageMixin, FormView):
    template_name = "core/register.html"
    form_class = RegisterForm
    success_message = "Your profile was created successfully!"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return redirect("core:login")


class HomeView(SuccessMessageMixin, View):
    def get(self, request):
        profile = User.objects.get(username="anil").profile
        project = profile.projects.all()[:3]
        return render(request, "core/home.html", {"profile": profile,
                                                   "projects": project})
    
class AboutView(SuccessMessageMixin, View):
    def get(self, request):
        about_me = User.objects.get(username="anil").profile.about_me
        social_links = about_me.links.all()
        return render(request, "core/about.html", {"about_me": about_me, "social_links": social_links})