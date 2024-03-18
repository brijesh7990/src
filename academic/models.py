from django.db import models
from base.models import BaseModel

# Create your models here.


class Standard(BaseModel):
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_standard"
    )
    standard = models.CharField(max_length=50)
    note = models.TextField(null=True, blank=True)
    subject = models.ManyToManyField("academic.Subject")

    def __str__(self):
        return self.standard


class Section(BaseModel):
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_section"
    )
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    standard = models.ForeignKey(
        "academic.Standard", on_delete=models.CASCADE, related_name="standard_section"
    )
    teacher = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subject(BaseModel):
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_subject"
    )
    subject_code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    teacher = models.ManyToManyField("user.User")

    def __str__(self):
        return self.name


class Syllabus(BaseModel):
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="syllabus"
    )
    standard = models.ForeignKey("academic.Standard", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    subject = models.ForeignKey("academic.Subject", on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/syllabus")

    def __str__(self):
        return self.title


class Assignment(BaseModel):
    school = models.ForeignKey("school.School", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField()
    standard = models.ForeignKey("academic.Standard", on_delete=models.CASCADE)
    section = models.ForeignKey("academic.Section", on_delete=models.CASCADE)
    subject = models.ForeignKey("academic.Subject", on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/assignment")


class Exam(BaseModel):
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_exam"
    )
    standard = models.ForeignKey(
        "academic.Standard", on_delete=models.CASCADE, related_name="standard_exam"
    )
    name = models.CharField(max_length=255)
    section = models.ForeignKey(
        "academic.Section", on_delete=models.CASCADE, related_name="section_exam"
    )
    subject = models.ForeignKey(
        "academic.Subject", on_delete=models.CASCADE, related_name="subject_exam"
    )
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    room = models.CharField(max_length=255)


class Grade(BaseModel):
    name = models.CharField(max_length=255)
    point = models.FloatField()
    mark_from = models.FloatField()
    mark_upto = models.FloatField()
    note = models.CharField(max_length=255)
