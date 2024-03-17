# Generated by Django 5.0.3 on 2024-03-17 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("point", models.FloatField()),
                ("mark_from", models.FloatField()),
                ("mark_upto", models.FloatField()),
                ("note", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Standard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("standard", models.CharField(max_length=50)),
                ("note", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("subject_code", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Syllabus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("file", models.FileField(upload_to="media/syllabus")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Assignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("deadline", models.DateField()),
                ("file", models.FileField(upload_to="media/assignment")),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.school"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("time_from", models.TimeField()),
                ("time_to", models.TimeField()),
                ("room", models.CharField(max_length=255)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="school_exam",
                        to="school.school",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("capacity", models.PositiveIntegerField()),
                ("note", models.TextField(blank=True, null=True)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="school_section",
                        to="school.school",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
