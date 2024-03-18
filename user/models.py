from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from user.manager import CustomUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.


class User(AbstractUser, BaseModel):
    SUPERADMIN = "superadmin"
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    PARENT = "parent"

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    APOS = "A+"
    ANEG = "A-"
    BPOS = "B+"
    BNEG = "B-"
    OPOS = "O+"
    ONEG = "O-"
    APPOS = "AP+"
    APNEG = "AP-"

    role_data = (
        (SUPERADMIN, "SuperAdmin"),
        (ADMIN, "Admin"),
        (TEACHER, "Teacher"),
        (STUDENT, "Student"),
        (PARENT, "Parent"),
    )

    gender_data = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    )

    blood_group_data = (
        (APOS, "A+"),
        (ANEG, "A-"),
        (BPOS, "B+"),
        (BNEG, "B-"),
        (OPOS, "O+"),
        (ONEG, "O-"),
        (APPOS, "AB+"),
        (APNEG, "AB-"),
    )

    dob = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_data, null=True, blank=True)
    blood_group = models.CharField(
        max_length=25, choices=blood_group_data, null=True, blank=True
    )
    phone = models.CharField(max_length=15)
    religion = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    role = models.CharField(max_length=25, choices=role_data)
    profile_pic = models.ImageField(
        upload_to="media/profilepics", null=True, blank=True
    )
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.username

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password", "role"]

    objects = CustomUserManager()


class SchoolUser(BaseModel):
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_user"
    )
    standard = models.ManyToManyField("academic.Standard")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username + " - " + self.school.name)


class Student(BaseModel):
    user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, related_name="standard_student"
    )
    standard = models.ForeignKey(
        "academic.Standard", on_delete=models.CASCADE, related_name="standard_student"
    )
    section = models.ForeignKey(
        "academic.Section", on_delete=models.CASCADE, related_name="standard_student"
    )
    school = models.ForeignKey("school.School", on_delete=models.CASCADE)


class Parent(BaseModel):
    user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, related_name="user_parent"
    )
    school = models.ForeignKey("school.School", on_delete=models.CASCADE)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    students = models.ManyToManyField("user.User")
    father_occupation = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)


class Teacher(BaseModel):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE)
    joining_date = models.DateTimeField()
    school = models.ForeignKey("school.School", on_delete=models.CASCADE)
