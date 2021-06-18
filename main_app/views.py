# from main_app.forms import SignUpForm
from typing import ContextManager
from main_app.models import Post, UserProfile
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

# forms
# from .forms import SignUpForm
from .forms import SignUpForm, UserProfileForm, LogInForm
# EditProfileForm

# auth imports
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get(self, request):
        form = SignUpForm()
        profile_form = UserProfileForm()
        log_in = LogInForm()
        context = {"form": form,
                   "profile_form": profile_form, "log_in": log_in}
        return render(request, "home.html", context)

    def post(self, request):
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        context = {"form": form, "profile_form": profile_form}

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            login(request, user)
            return redirect("accounts/profile")
        else:


           # else statement does not seem to have any impact
            return redirect("signup")

    def post(self, request):
        log_in = LogInForm(request.POST)

        if log_in.is_valid():
            user = log_in.save()

            login(request, user)
            return redirect("accounts/profile")
        else:


           # else statement does not seem to have any impact

            return redirect("home")


# This functions but doesn't have extra fields we need, keeping as a backup


class Signup(TemplateView):

    def get(self, request):
        form = SignUpForm()
        profile_form = UserProfileForm()
        context = {"form": form, "profile_form": profile_form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            login(request, user)
            return redirect("login")
        else:
            return redirect("signup")


# def showslides(request):
 #   return render(request, 'home.html')


class Profile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


# UpdateView automatically makes a form

class EditProfile(UpdateView):
    model = UserProfile
    template_name = "edit_profile.html"

    fields = ['current_city']

    success_url = "/profile/"

    # def get(self, request):
    #     edit_form = EditProfileForm()
    #     context = {"edit_form": edit_form}
    #     return render(request, "edit_profile.html", context)

    # def post(self, request):
    #     edit_form = EditProfileForm(request.POST)
    #     edit_form.save()

    #     return redirect("profile")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["userprofile"] = UserProfile.objects.all()
    #     return context

    # def get_success_url(self):
    #     return reverse('', kwargs={'pk': self.object.pk})


# original form ------
# class Signup(View):
#     def get(self, request):
#         form = SignUpForm()
#         profile_form = UserProfileForm()
#         context = {"form": form}
#         return render(request, "signup.html", context)

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("login")
#         else:
#             context = {"form": form}
#             print(form.errors, "Failed to sign-up user")
#             return render(request, "signup.html", context)

# 2nd attempt below


# class Signup(TemplateView):
#     def get(self, request):
#         # form = UserCreationForm
#         form = SignUpForm()
#         # profile_form = UserProfileForm(request.POST)
#         context = {"form": form}
#         return render(request, "signup.html", context)

#     def post(self, request):
#         # form = UserCreationForm
#         form = SignUpForm(request.POST)


# # If it breaks takeout the profile_form part
#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()


# # commit = false makes so it doesn't save to database right away

#             profile = profile_form.save(commit=False)
#             profile.user = user

#             profile.save()

#             login(request, user)

#             return redirect("profile")

#         else:
#             context = {'form': form, 'profile_form': profile_form}
#             print(form.errors, "Failed to sign-up user")
#             return render(request, "signup.html", context)

# 3rd attempt

# def Signup(request):

#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         profile_form = UserProfileForm(request.POST)

#         if form.is_valid() and profile_form.is_valid():
#             form.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user

#             profile.save()


#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)

#             return redirect('index')
#     else:
#         form = SignUpForm()
#         profile_form = UserProfileForm()

#     context = {'form' : form, 'profile_form' : profile_form}
