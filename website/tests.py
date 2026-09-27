from pathlib import Path

from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from .management.commands.seed_demo import PROJECTS, SERVICES
from .models import BlogPost, FAQItem, NewsletterSubscriber, PortfolioProject, Service


@override_settings(
    STORAGES={
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class DynamicContentTests(TestCase):
    def test_seeded_images_resolve_to_deployable_static_files(self):
        post = BlogPost(
            title="Image fallback",
            slug="image-fallback",
            excerpt="Excerpt",
            content="Content",
            cover_image="blog/1_branding-mockup.jpg",
        )
        project = PortfolioProject(
            title="Image fallback",
            slug="image-fallback-project",
            category="Branding",
            image="portfolio/6_tivra-brand.jpg",
        )

        self.assertEqual(post.image_url, "/static/site/images/1_branding-mockup.jpg")
        self.assertEqual(project.image_url, "/static/site/images/6_tivra-brand.jpg")

        missing_project_image = PortfolioProject(
            title="Missing image",
            slug="missing-image",
            category="Branding",
            image="portfolio/not-deployed.png",
        )
        self.assertEqual(
            missing_project_image.image_url,
            "/static/site/images/portfolio-hero.webp",
        )

    def test_blog_listing_and_detail_use_static_image_fallback(self):
        post = BlogPost.objects.create(
            title="Image fallback",
            slug="image-fallback",
            excerpt="A short excerpt.",
            content="Article content.",
            cover_image="blog/1_branding-mockup.jpg",
            published_at=timezone.now(),
        )

        listing = self.client.get(reverse("blog"))
        detail = self.client.get(reverse("blog_detail", args=[post.slug]))

        self.assertContains(listing, "/static/site/images/1_branding-mockup.jpg")
        self.assertContains(detail, "/static/site/images/1_branding-mockup.jpg")

    def test_cgi_ad_service_shows_image_gallery_and_playable_video(self):
        data = next(item for item in SERVICES if item["slug"] == "cgi-ad-creation")
        service = Service.objects.create(**data, order=7)

        listing = self.client.get(reverse("services"))
        detail = self.client.get(reverse("service_detail", args=[service.slug]))

        self.assertContains(listing, "CGI Ad Creation")
        self.assertContains(detail, "CGI Showcase")
        self.assertContains(detail, "CGI AD CREATION")
        self.assertContains(detail, "NAKRANI PRODUCTION")
        self.assertContains(detail, "<video")
        self.assertContains(detail, "autoplay muted loop")
        self.assertNotContains(detail, "controls")
        self.assertContains(
            detail,
            "/static/site/videos/cgi-helicopter-ad.mp4",
        )
        self.assertContains(
            detail,
            "/static/site/images/cgi-helicopter-ad-poster.jpeg",
        )
        for image_path in service.gallery_image_list:
            self.assertTrue(
                (
                    Path(settings.STATICFILES_DIRS[0])
                    / Path(*image_path.split("/"))
                ).is_file()
            )
            self.assertContains(detail, f"/static/{image_path}")
        self.assertTrue(
            (
                Path(settings.STATICFILES_DIRS[0])
                / "site"
                / "videos"
                / "cgi-helicopter-ad.mp4"
            ).is_file()
        )

    def test_portfolio_related_work_uses_static_image_fallback_and_scroll_parallax(self):
        PortfolioProject.objects.create(
            title="Orbit project",
            slug="orbit-project",
            category="Digital Design",
            active=True,
        )
        PortfolioProject.objects.create(
            title="Related project",
            slug="related-project",
            category="Branding",
            image="portfolio/6_tivra-brand.jpg",
            active=True,
        )

        response = self.client.get(reverse("portfolio_detail", args=["orbit-project"]))

        self.assertContains(response, "/static/site/images/6_tivra-brand.jpg")
        self.assertContains(response, "window.addEventListener('scroll', scheduleParallax")
        self.assertContains(response, "layer.style.translate = (mouseX * depth).toFixed(2)")

    def test_all_site_pages_include_shared_scroll_parallax(self):
        service = Service.objects.create(
            title="Parallax service",
            slug="parallax-service",
            description="Service description.",
        )
        project = PortfolioProject.objects.create(
            title="Parallax project",
            slug="parallax-project",
            category="Branding",
        )
        post = BlogPost.objects.create(
            title="Parallax article",
            slug="parallax-article",
            excerpt="A short excerpt.",
            content="Article content.",
            published_at=timezone.now(),
        )
        paths = [
            reverse("home"),
            reverse("about"),
            reverse("services"),
            reverse("service_detail", args=[service.slug]),
            reverse("portfolio"),
            reverse("portfolio_detail", args=[project.slug]),
            reverse("blog"),
            reverse("blog_detail", args=[post.slug]),
            reverse("contact"),
        ]

        for path in paths:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(
                    response,
                    "window.addEventListener('scroll', scheduleParallax",
                )
                self.assertContains(response, "data-depth=")

    def test_services_heroes_match_portfolio_background_treatment(self):
        service = Service.objects.create(
            title="Branding & Identity",
            slug="branding-identity",
            description="Build a distinctive brand identity.",
        )
        for path, background_class, shade_class in (
            (
                reverse("services"),
                "services-hero-bg",
                "services-hero-shade",
            ),
            (
                reverse("service_detail", args=[service.slug]),
                "d-hero-bg",
                "d-hero-shade",
            ),
        ):
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertContains(response, f'class="{background_class}"')
                self.assertContains(response, "opacity: .2")
                self.assertContains(response, f'class="{shade_class}"')
                self.assertContains(
                    response,
                    "linear-gradient(to bottom, rgba(10,10,10,.8), "
                    "rgba(10,10,10,.6), rgba(10,10,10,.9))",
                )
                self.assertContains(
                    response,
                    "/static/site/images/hero-bg.webp",
                )

    def test_vasani_natural_brand_project_shows_all_images_in_identity_gallery(self):
        data = next(item for item in PROJECTS if item["slug"] == "vasani-natural-branding")
        gallery_images = data["gallery_images"].splitlines()
        project = PortfolioProject.objects.create(
            title=data["title"],
            slug=data["slug"],
            category=data["category"],
            description=data["description"],
            design_details=data["design_details"],
            provided_services=data["provided_services"],
            challenge=data["challenge"],
            solution=data["solution"],
            result=data["result"],
            client=data["client"],
            year=data["year"],
            image=f"portfolio/{data['image']}",
            gallery_images=data["gallery_images"],
        )

        response = self.client.get(reverse("portfolio_detail", args=[project.slug]))

        self.assertEqual(len(gallery_images), 11)
        self.assertEqual(len(response.context["gallery_images"]), 11)
        self.assertEqual(len(response.context["gallery_sections"]), 1)
        self.assertEqual(len(response.context["gallery_sections"][0]["images"]), 11)
        self.assertContains(response, "Brand Identity")
        self.assertNotContains(response, "Brand Applications")
        self.assertContains(response, "pd-cover-frame--vasani")
        self.assertEqual(
            response.content.decode().count(
                "/static/site/images/vasani-natural-products-billboard.jpeg"
            ),
            2,
        )
        for image_path in gallery_images:
            asset_path = image_path.removeprefix("site/images/")
            self.assertTrue(
                (Path(settings.STATICFILES_DIRS[0]) / "site" / "images" / asset_path).is_file()
            )
            self.assertContains(response, f"/static/{image_path}")
        self.assertContains(response, "/static/site/images/vasani-natural-products-billboard.jpeg")

    def test_contact_page_renders_active_database_faqs(self):
        FAQItem.objects.create(
            page="contact",
            question="Can you help with a launch?",
            answer="Yes, we can support your launch.",
        )
        FAQItem.objects.create(
            page="contact",
            question="Hidden question",
            answer="This item is inactive.",
            active=False,
        )

        response = self.client.get(reverse("contact"))

        self.assertContains(response, "Can you help with a launch?")
        self.assertContains(response, "Yes, we can support your launch.")
        self.assertNotContains(response, "Hidden question")

    def test_blog_newsletter_subscribes_and_reactivates_email(self):
        subscriber = NewsletterSubscriber.objects.create(
            email="reader@example.com",
            active=False,
        )

        response = self.client.post(
            reverse("blog"),
            {"email": "reader@example.com"},
        )

        self.assertRedirects(response, reverse("blog"))
        subscriber.refresh_from_db()
        self.assertTrue(subscriber.active)
        self.assertEqual(NewsletterSubscriber.objects.count(), 1)

    def test_blog_rejects_invalid_newsletter_email(self):
        response = self.client.post(reverse("blog"), {"email": "not-an-email"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a valid email address.")
        self.assertFalse(NewsletterSubscriber.objects.exists())

    def test_service_detail_uses_database_copy_fields(self):
        service = Service.objects.create(
            title="Custom service",
            slug="custom-service",
            description="Service description.",
            detail_heading="A custom heading",
            detail_intro="First paragraph.\nSecond paragraph.",
            features="Brand strategy",
            feature_descriptions="Research shaped around the client.",
            process="Discover",
            process_descriptions="We learn about the client's goals.",
        )

        response = self.client.get(reverse("service_detail", args=[service.slug]))

        self.assertContains(response, "A custom heading")
        self.assertContains(response, "First paragraph.")
        self.assertContains(response, "Research shaped around the client.")
        self.assertContains(response, "We learn about the client&#x27;s goals.")
