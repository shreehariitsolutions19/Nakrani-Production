from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("website", "0004_fix_non_nullable_timestamps")]

    operations = [
        migrations.AddField(
            model_name="contactsubmission",
            name="company",
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name="contactsubmission",
            name="project_timeline",
            field=models.CharField(blank=True, max_length=160),
        ),
    ]
