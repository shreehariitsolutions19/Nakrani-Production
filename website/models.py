from pathlib import Path

from django.conf import settings
from django.db import models
from django.templatetags.static import static
from django.utils.text import slugify


def resolve_image_url(image_field, fallback_static_path="site/images/portfolio-hero.webp"):
    if not image_field or not getattr(image_field, "name", ""):
        return static(fallback_static_path)

    image_name = Path(image_field.name).name
    static_images_dir = Path(settings.STATICFILES_DIRS[0]) / "site" / "images"
    if (static_images_dir / image_name).exists():
        return static(f"site/images/{image_name}")

    if image_field.storage.exists(image_field.name):
        return image_field.url

    return static(fallback_static_path)


class SiteSettings(models.Model):
    brand_name = models.CharField(max_length=120, default="Nakrani Production")
    owner_name = models.CharField(max_length=120, default="Hitul Nakrani")
    tagline = models.CharField(max_length=255, default="We combine creativity, strategy and design to create stunning visuals that inspire and engage.")
    phone = models.CharField(max_length=40, default="+91 70162 28333")
    email = models.EmailField(default="Design.Hitul@gmail.com")
    city = models.CharField(max_length=120, default="Visnagar, Mehsana, Gujarat, India")
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
    feature_descriptions = models.TextField(
        blank=True,
        help_text="One description per feature line",
    )
    process = models.TextField(blank=True, help_text="One process step per line")
    process_descriptions = models.TextField(
        blank=True,
        help_text="One description per process line",
    )
    detail_heading = models.CharField(max_length=180, blank=True)
    detail_intro = models.TextField(
        blank=True,
        help_text="One paragraph per line",
    )
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

    @property
    def feature_description_list(self):
        return [x.strip() for x in self.feature_descriptions.splitlines() if x.strip()]

    @property
    def process_description_list(self):
        return [x.strip() for x in self.process_descriptions.splitlines() if x.strip()]

    @property
    def detail_intro_list(self):
        return [x.strip() for x in self.detail_intro.splitlines() if x.strip()]

    @property
    def feature_item_list(self):
        descriptions = self.feature_description_list
        return [
            {
                "title": feature,
                "description": descriptions[index] if index < len(descriptions) and descriptions[index]
                else "Thoughtful, production-ready visual work tailored to your brand.",
            }
            for index, feature in enumerate(self.feature_list)
        ]

    @property
    def process_item_list(self):
        descriptions = self.process_description_list
        return [
            {
                "title": step,
                "description": descriptions[index] if index < len(descriptions) and descriptions[index]
                else "Focused collaboration and careful execution at every stage.",
            }
            for index, step in enumerate(self.process_list)
        ]

    @property
    def image_url(self):
        return resolve_image_url(self.image, "site/images/services-hero.webp")

    def __str__(self):
        return self.title


class PortfolioProject(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    category = models.CharField(max_length=80)
    image = models.ImageField(upload_to="portfolio/", blank=True)
    description = models.TextField(blank=True)
    design_details = models.TextField(blank=True)
    provided_services = models.TextField(blank=True, help_text="One service per line")
    challenge = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    result = models.TextField(blank=True)
    gallery_images = models.TextField(blank=True, help_text="One static image path per line")
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

    @property
    def image_url(self):
        return resolve_image_url(self.image, "site/images/portfolio-hero.webp")

    def __str__(self):
        return self.title

    @property
    def provided_service_list(self):
        return [item.strip() for item in self.provided_services.splitlines() if item.strip()]

    @property
    def gallery_image_list(self):
        return [item.strip() for item in self.gallery_images.splitlines() if item.strip()]


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
    read_time = models.PositiveSmallIntegerField(default=6)
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

    @property
    def image_url(self):
        return resolve_image_url(
            self.cover_image,
            "site/images/blog-detail-hero.webp",
        )

    def __str__(self):
        return self.title


class PageContent(models.Model):
    page = models.CharField(max_length=40)
    key = models.SlugField(max_length=100, unique=True)
    value = models.TextField(blank=True)
    image = models.ImageField(upload_to="page-content/", blank=True)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Page content"
        verbose_name_plural = "Page content"
        ordering = ["page", "key"]

    def __str__(self):
        return f"{self.page}: {self.key}"


class PageContentItem(models.Model):
    page = models.CharField(max_length=40)
    section = models.CharField(max_length=60)
    title = models.CharField(max_length=180)
    eyebrow = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    value = models.CharField(max_length=180, blank=True)
    icon_class = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to="page-content/items/", blank=True)
    button_text = models.CharField(max_length=80, blank=True)
    button_url = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["page", "section", "order", "id"]

    def __str__(self):
        return f"{self.page}: {self.section}: {self.title}"


class FAQItem(models.Model):
    page = models.CharField(max_length=40, default="contact")
    question = models.CharField(max_length=240)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ item"
        verbose_name_plural = "FAQ items"
        ordering = ["page", "order", "id"]

    def __str__(self):
        return self.question


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-subscribed_at"]

    def __str__(self):
        return self.email


class ContactSubmission(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    city = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.name} — {self.email}"
