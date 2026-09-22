from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("website", "0002_complete_fields")]

    operations = [
        migrations.AddField(model_name="sitesettings", name="address", field=models.CharField(blank=True, max_length=255)),
        migrations.AddField(model_name="sitesettings", name="facebook", field=models.URLField(blank=True)),
        migrations.AddField(model_name="sitesettings", name="favicon", field=models.ImageField(blank=True, upload_to="site/")),
        migrations.AddField(model_name="sitesettings", name="logo", field=models.ImageField(blank=True, upload_to="site/")),
        migrations.AddField(model_name="sitesettings", name="meta_description", field=models.TextField(default="Premium branding, web, print, packaging and social media design.")),
        migrations.AddField(model_name="sitesettings", name="meta_title", field=models.CharField(default="Nakrani Production — Premium Graphic Design Agency", max_length=180)),
        migrations.AddField(model_name="service", name="created_at", field=models.DateTimeField(auto_now_add=True, null=True)),
        migrations.AddField(model_name="service", name="features", field=models.TextField(blank=True, help_text="One feature per line")),
        migrations.AddField(model_name="service", name="image", field=models.ImageField(blank=True, upload_to="services/")),
        migrations.AddField(model_name="service", name="process", field=models.TextField(blank=True, help_text="One process step per line")),
        migrations.AddField(model_name="service", name="updated_at", field=models.DateTimeField(auto_now=True, null=True)),
        migrations.AddField(model_name="portfolioproject", name="design_details", field=models.TextField(blank=True)),
        migrations.AddField(model_name="portfolioproject", name="created_at", field=models.DateTimeField(auto_now_add=True, null=True)),
        migrations.AddField(model_name="portfolioproject", name="updated_at", field=models.DateTimeField(auto_now=True, null=True)),
        migrations.AddField(model_name="testimonial", name="company", field=models.CharField(blank=True, max_length=160)),
        migrations.AddField(model_name="testimonial", name="rating", field=models.PositiveSmallIntegerField(default=5)),
        migrations.AddField(model_name="blogpost", name="published", field=models.BooleanField(default=True)),
        migrations.AlterField(model_name="blogpost", name="slug", field=models.SlugField(blank=True, max_length=190, unique=True)),
    ]
