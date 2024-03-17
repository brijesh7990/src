from django.contrib import admin

from academic.models import (
    Assignment,
    Exam,
    Grade,
    Section,
    Standard,
    Subject,
    Syllabus,
)

# Register your models here.

admin.site.register([Standard, Section, Subject, Syllabus, Assignment, Exam, Grade])
