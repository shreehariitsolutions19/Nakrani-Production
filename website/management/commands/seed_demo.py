from datetime import timedelta
from pathlib import Path
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from website.models import SiteSettings, Service, PortfolioProject, Testimonial, BlogPost


class Command(BaseCommand):
    help = "Seed reference-matched demo content and copy the captured reference images into media."

    def copy_demo_image(self, filename, folder):
        src = Path(settings.BASE_DIR) / "website" / "static" / "site" / "images" / filename
        dest_dir = Path(settings.MEDIA_ROOT) / folder
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / filename
        if src.exists() and not dest.exists():
            shutil.copy2(src, dest)
        return f"{folder}/{filename}" if src.exists() else ""

    def handle(self, *args, **options):
        SiteSettings.objects.update_or_create(pk=1, defaults={
            "brand_name": "Nakrani Production",
            "owner_name": "Hitul Nakrani",
            "tagline": "We create stunning visual experiences that inspire and engage. Premium design for premium brands.",
            "phone": "+91 70162 28333",
            "email": "Design.Hitul@gmail.com",
            "city": "Visnagar, Mehsana, Gujarat, India",
            "address": "Visnagar, Mehsana, Gujarat, India",
            "facebook": "https://www.facebook.com/",
            "linkedin": "https://www.linkedin.com/",
            "instagram": "https://www.instagram.com/",
            "twitter": "https://x.com/",
            "meta_title": "Nakrani Production — Premium Graphic Design Agency",
            "meta_description": "Premium graphic design, branding, packaging, print and social media design.",
        })

        services = [
            ("Branding & Identity", "ri-palette-line", "We create strong brand identities that make your business stand out from the crowd. From logos to complete brand systems."),
            ("Web Design", "ri-computer-line", "We design modern, responsive and user-friendly websites that deliver results and elevate your digital presence."),
            ("Print Design", "ri-file-list-3-line", "From brochures to posters, we design print materials that communicate your message with elegance and impact."),
            ("Social Media Design", "ri-share-line", "We create eye-catching social media designs that boost engagement, grow brands, and drive meaningful conversations."),
        ]
        for i, (title, icon, desc) in enumerate(services, 1):
            Service.objects.update_or_create(title=title, defaults={
                "icon_class": icon, "description": desc, "order": i,
                "features": "Creative direction\nVisual identity system\nProduction-ready assets\nBrand guidelines",
                "process": "Discover\nStrategy\nDesign\nRefine\nDeliver",
                "active": True,
            })

        project_data = [
            ("MOON Cosmetics", "Branding", "A refined identity and packaging direction for a modern cosmetics label.", "4_moon-cosmetics.jpg"),
            ("Aura Packaging", "Packaging", "Premium packaging concepts built around clarity, material and shelf impact.", "5_aura-packaging.jpg"),
            ("Tivra Brand", "Identity", "A bold identity system balancing contemporary typography and distinctive forms.", "6_tivra-brand.jpg"),
            ("Cereal Editorial", "Print Design", "Editorial design with a strong grid, expressive type and tactile rhythm.", "7_cereal-editorial.jpg"),
            ("Lumina Label", "Label Design", "Elegant label artwork created for a premium product collection.", "8_lumina-label.jpg"),
            ("TATTVA", "Branding", "A cohesive visual identity with a warm, sophisticated brand language.", "9_tattva.png"),
        ]
        for i, (title, cat, desc, image) in enumerate(project_data, 1):
            PortfolioProject.objects.update_or_create(title=title, defaults={
                "category": cat, "description": desc,
                "design_details": "Concept direction, typography, layout, color and production details.",
                "client": title + " Client", "year": 2026, "featured": True, "order": i,
                "active": True, "image": self.copy_demo_image(image, "portfolio"),
            })

        Testimonial.objects.update_or_create(client_name="Ravi Patel", defaults={
            "role": "Founder", "company": "Urban Style",
            "quote": "Nakrani Production understood our vision perfectly and delivered a brand identity that truly represents our business. Highly professional and creative team!",
            "rating": 5, "active": True,
            "photo": self.copy_demo_image("10_ravi-patel.jpg", "testimonials"),
        })

        now = timezone.now()
        posts = [
            ("How a strong visual identity builds brand memory", "Branding", "A practical look at the visual choices that help brands become recognizable.", "Start with a clear idea. Build a flexible system around it. Then apply it consistently across every touchpoint."),
            ("Packaging design: balancing shelf impact and clarity", "Packaging", "How hierarchy, typography and structure can make packaging easier to understand.", "Good packaging needs to be distinctive at a distance and useful up close. The strongest concepts balance both."),
            ("Designing social content that still feels like a brand", "Social Media", "A framework for building repeatable social creatives without losing personality.", "Create a visual toolkit first, then design individual posts inside that system."),
        ]
        blog_images = ["7_cereal-editorial.jpg", "5_aura-packaging.jpg", "2_creative-agency-mockup.jpg"]
        for i, (title, cat, excerpt, content) in enumerate(posts):
            BlogPost.objects.update_or_create(title=title, defaults={
                "category": cat, "excerpt": excerpt, "content": content,
                "author": "Nakrani Production", "published": True,
                "published_at": now - timedelta(days=i), "active": True,
                "cover_image": self.copy_demo_image(blog_images[i], "blog"),
            })
        self.stdout.write(self.style.SUCCESS("Reference-matched demo content is ready."))
