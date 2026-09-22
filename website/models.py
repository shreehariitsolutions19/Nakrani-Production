from django.db import models
from django.utils.text import slugify


class SiteSettings(models.Model):
    brand_name = models.CharField(max_length=120, default="Nakrani Production")
    tagline = models.CharField(max_length=255, default="We combine creativity, strategy and design to create stunning visuals that inspire and engage.")
    phone = models.CharField(max_length=40, default="+91 98765 43210")
    email = models.EmailField(default="hello@nakrani.production")
    city = models.CharField(max_length=120, default="Mumbai, India")
    address = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to="site/", blank=True)
    favicon = models.ImageField(upload_to="site/", blank=True)
    google_form_url = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    meta_title = models.CharField(max_length=180, default="Nakrani Production — Premium Graphic Design Agency")
    meta_description = models.TextField(default="Premium branding, web, print, packaging and social media design.")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.brand_name


class Service(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    description = models.TextField()
    icon_class = models.CharField(max_length=80, default="ri-palette-line")
    image = models.ImageField(upload_to="services/", blank=True)
    features = models.TextField(blank=True, help_text="One feature per line")
    process = models.TextField(blank=True, help_text="One process step per line")
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def feature_list(self):
        return [x.strip() for x in self.features.splitlines() if x.strip()]

    @property
    def process_list(self):
        return [x.strip() for x in self.process.splitlines() if x.strip()]

    def __str__(self):
        return self.title


class PortfolioProject(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    category = models.CharField(max_length=80)
    image = models.ImageField(upload_to="portfolio/", blank=True)
    description = models.TextField(blank=True)
    design_details = models.TextField(blank=True)
    client = models.CharField(max_length=160, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    company = models.CharField(max_length=160, blank=True)
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    photo = models.ImageField(upload_to="testimonials/", blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class BlogPost(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=190, unique=True, blank=True)
    excerpt = models.TextField(max_length=320)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="blog/", blank=True)
    author = models.CharField(max_length=120, default="Nakrani Production")
    category = models.CharField(max_length=80, default="Design")
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    project_type = models.CharField(max_length=120, blank=True)
    budget = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=30, default="new")
    source = models.CharField(max_length=40, default="website")
    google_synced = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.email}"
