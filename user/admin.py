from django.contrib import admin

from user.models import SchoolUser, Student, Teacher, User, Parent

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django import forms

# Register your models here.


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def clean_password(self):
        # Hash the password if a new password is provided
        password = self.cleaned_data.get("password")
        if password:
            return make_password(password)
        return password


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserForm


admin.site.register(User, CustomUserAdmin)
admin.site.register([SchoolUser, Parent, Teacher, Student])
