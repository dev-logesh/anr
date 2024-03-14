# Generated by Django 5.0.3 on 2024-03-14 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("batch", "0001_initial"),
        ("corecode", "0001_initial"),
        ("staffs", "0001_initial"),
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="batchmodel",
            name="batch_course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="corecode.subject",
                verbose_name="Batch subject",
            ),
        ),
        migrations.AddField(
            model_name="batchmodel",
            name="batch_staff",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="staffs.staff"
            ),
        ),
        migrations.AddField(
            model_name="batchmodel",
            name="batch_students",
            field=models.ManyToManyField(blank=True, to="students.student"),
        ),
        migrations.AddField(
            model_name="batchmodel",
            name="batch_timing",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="corecode.time",
                verbose_name="Class Timing",
            ),
        ),
    ]