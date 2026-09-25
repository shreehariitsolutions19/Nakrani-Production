from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0011_set_default_social_links"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactsubmission",
            name="city",
            field=models.CharField(default="", max_length=120),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="company",
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="google_synced",
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="message",
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="project_timeline",
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="project_type",
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="budget",
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="source",
        ),
        migrations.RemoveField(
            model_name="contactsubmission",
            name="status",
        ),
    ]
