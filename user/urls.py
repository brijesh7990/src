from django import forms
from django.contrib.auth.views import LoginView,LogoutView
from user.forms import CustomAuthenticationForm
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .forms import CustomAuthenticationForm,CustomPasswordResetForm,CustomPasswordSetForm


urlpatterns = [
    path("accounts/login/", LoginView.as_view(authentication_form=CustomAuthenticationForm), name="login"),
    path("accounts/logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    # path("updateprofile/<pk>/", views.UpdateProfileView.as_view(), name="updateprofile"),

    path('accounts/password_reset/',PasswordResetView.as_view(form_class=CustomPasswordResetForm),name="password_reset"),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(form_class=CustomPasswordSetForm),name='password_reset_confirm'),
    path('accounts/reset/done/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]