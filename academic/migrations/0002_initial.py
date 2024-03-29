# Generated by Django 5.0.3 on 2024-03-17 12:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("academic", "0001_initial"),
        ("school", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="section",
            name="teacher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="exam",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="section_exam",
                to="academic.section",
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.section"
            ),
        ),
        migrations.AddField(
            model_name="standard",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="school_standard",
                to="school.school",
            ),
        ),
        migrations.AddField(
            model_name="section",
            name="standard",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="standard_section",
                to="academic.standard",
            ),
        ),
        migrations.AddField(
            model_name="exam",
            name="standard",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="standard_exam",
                to="academic.standard",
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="standard",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.standard"
            ),
        ),
        migrations.AddField(
            model_name="subject",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="school_subject",
                to="school.school",
            ),
        ),
        migrations.AddField(
            model_name="subject",
            name="teacher",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="standard",
            name="subject",
            field=models.ManyToManyField(to="academic.subject"),
        ),
        migrations.AddField(
            model_name="exam",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subject_exam",
                to="academic.subject",
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.subject"
            ),
        ),
        migrations.AddField(
            model_name="syllabus",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="syllabus",
                to="school.school",
            ),
        ),
        migrations.AddField(
            model_name="syllabus",
            name="standard",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.standard"
            ),
        ),
        migrations.AddField(
            model_name="syllabus",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.subject"
            ),
        ),
    ]
