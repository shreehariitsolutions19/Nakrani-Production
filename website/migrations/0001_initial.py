from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteSettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("brand_name", models.CharField(default="Nakrani Production", max_length=120)),
                ("tagline", models.CharField(default="We create stunning visual experiences that inspire and engage.", max_length=255)),
                ("phone", models.CharField(default="+91 98765 43210", max_length=40)),
                ("email", models.EmailField(default="hello@nakrani.production", max_length=254)),
                ("city", models.CharField(default="Mumbai, India", max_length=120)),
                ("google_form_url", models.URLField(blank=True)),
                ("instagram", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("twitter", models.URLField(blank=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Site settings", "verbose_name_plural": "Site settings"},
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField()),
                ("icon_class", models.CharField(default="ri-palette-line", max_length=80)),
                ("order", models.PositiveIntegerField(default=0)),
                ("active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="PortfolioProject",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("category", models.CharField(max_length=80)),
                ("image", models.ImageField(blank=True, upload_to="portfolio/")),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("client_name", models.CharField(max_length=120)),
                ("role", models.CharField(blank=True, max_length=120)),
                ("quote", models.TextField()),
                ("photo", models.ImageField(blank=True, upload_to="testimonials/")),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("slug", models.SlugField(max_length=190, unique=True)),
                ("excerpt", models.TextField(max_length=320)),
                ("content", models.TextField()),
                ("cover_image", models.ImageField(blank=True, upload_to="blog/")),
                ("category", models.CharField(default="Design", max_length=80)),
                ("published_at", models.DateTimeField()),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-published_at", "-id"]},
        ),
        migrations.CreateModel(
            name="ContactSubmission",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("message", models.TextField()),
                ("source", models.CharField(default="website", max_length=40)),
                ("google_synced", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
