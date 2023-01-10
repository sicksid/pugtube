# Generated by Django 4.1 on 2023-01-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="upload",
            name="duration",
            field=models.IntegerField(
                blank=True, help_text="Duration of the video in seconds", null=True
            ),
        ),
        migrations.AddField(
            model_name="upload",
            name="file_type",
            field=models.CharField(
                blank=True,
                help_text="File type of the video, e.g. mp4, webm, etc.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="upload",
            name="fps",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="height",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="original",
            field=models.CharField(
                blank=True,
                help_text="Original link to the file",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="upload",
            name="quality",
            field=models.CharField(
                blank=True,
                help_text="Quality of the video, e.g. hd, sd, etc.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="upload",
            name="width",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]