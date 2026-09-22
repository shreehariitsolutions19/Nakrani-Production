from django.contrib import admin
from django.utils.html import format_html

from .models import BlogPost, ContactSubmission, PortfolioProject, Service, SiteSettings, Testimonial


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "email", "phone", "city", "updated_at")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "active")
    list_editable = ("order", "active")
    search_fields = ("title", "description")


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ("thumb", "title", "category", "order", "active")
    list_editable = ("order", "active")
    search_fields = ("title", "category", "description")
    list_filter = ("category", "active")

    @admin.display(description="Image")
    def thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="58" height="42" style="object-fit:cover;border-radius:6px;" />', obj.image.url)
        return "—"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("client_name", "role", "active", "created_at")
    list_editable = ("active",)
    search_fields = ("client_name", "role", "quote")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at", "active")
    list_editable = ("active",)
    search_fields = ("title", "slug", "excerpt", "content")
    list_filter = ("category", "active")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "source", "google_synced", "created_at")
    readonly_fields = ("created_at", "google_synced")
    search_fields = ("name", "email", "phone", "message")
    list_filter = ("google_synced", "source")
