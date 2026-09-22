from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [('website','0001_initial')]
    operations = [
        migrations.AddField(model_name='service', name='slug', field=models.SlugField(blank=True, max_length=140, unique=True)),
        migrations.AddField(model_name='portfolioproject', name='slug', field=models.SlugField(blank=True, max_length=180, unique=True)),
        migrations.AddField(model_name='portfolioproject', name='client', field=models.CharField(blank=True, max_length=160)),
        migrations.AddField(model_name='portfolioproject', name='year', field=models.PositiveIntegerField(blank=True, null=True)),
        migrations.AddField(model_name='portfolioproject', name='featured', field=models.BooleanField(default=False)),
        migrations.AddField(model_name='blogpost', name='author', field=models.CharField(default='Nakrani Production', max_length=120)),
        migrations.AddField(model_name='contactsubmission', name='project_type', field=models.CharField(blank=True, max_length=120)),
        migrations.AddField(model_name='contactsubmission', name='budget', field=models.CharField(blank=True, max_length=120)),
        migrations.AddField(model_name='contactsubmission', name='status', field=models.CharField(default='new', max_length=30)),
    ]
