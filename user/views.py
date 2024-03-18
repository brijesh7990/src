from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from user.models import User
# from user.forms import   # Import the missing UpdateProfileForm class


# Create your views here.

# class UpdateProfileView(UpdateView):
#     model = User
#     form_class = 
#     fields = ["first_name", "last_name", "email", "phone", "address", "profile_pic"]
#     success_url = reverse_lazy("dashboard")
#     template_name = "users/updateprofile.html"