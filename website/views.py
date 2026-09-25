import requests
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import BlogPost, ContactSubmission, PortfolioProject, Service, SiteSettings, Testimonial


def site_context():
    return {
        "site_settings": SiteSettings.objects.first(),
        "services": Service.objects.filter(active=True),
        "projects": PortfolioProject.objects.filter(active=True),
        "testimonials": Testimonial.objects.filter(active=True),
    }


def home(request):
    context = site_context()
    context.update({
        "page_title": "Home",
        "featured_projects": PortfolioProject.objects.filter(active=True, featured=True)[:6],
        "posts": BlogPost.objects.filter(active=True, published=True, published_at__lte=timezone.now())[:3],
    })
    return render(request, "website/home.html", context)


def about(request):
    context = site_context()
    context["page_title"] = "About Us"
    return render(request, "website/about.html", context)


def services(request):
    context = site_context()
    context["page_title"] = "Services"
    return render(request, "website/services.html", context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, active=True)
    context = site_context()
    context.update({"page_title": service.title, "service": service})
    context["related_projects"] = PortfolioProject.objects.filter(active=True)[:3]
    return render(request, "website/service_detail.html", context)


def portfolio(request):
    context = site_context()
    selected_category = request.GET.get("category", "").strip()
    projects = PortfolioProject.objects.filter(active=True)
    if selected_category:
        projects = projects.filter(category__iexact=selected_category)
    context.update({
        "page_title": "Portfolio",
        "projects": projects,
        "selected_category": selected_category,
        "categories": PortfolioProject.objects.filter(active=True).values_list("category", flat=True).distinct(),
        "featured_project": PortfolioProject.objects.filter(active=True, featured=True).first()
            or PortfolioProject.objects.filter(active=True).first(),
    })
    return render(request, "website/portfolio.html", context)


def portfolio_detail(request, slug):
    project = get_object_or_404(PortfolioProject, slug=slug, active=True)
    context = site_context()
    active_projects = PortfolioProject.objects.filter(active=True).order_by("order", "id")

    fallback_gallery = {
        "moon-cosmetics": [
            "site/images/4_moon-cosmetics.jpg",
            "site/images/3_stationery-mockup.jpg",
            "site/images/2_creative-agency-mockup.jpg",
        ],
        "aura-packaging": [
            "site/images/5_aura-packaging.jpg",
            "site/images/3_stationery-mockup.jpg",
            "site/images/1_branding-mockup.jpg",
        ],
        "tivra-brand": [
            "site/images/6_tivra-brand.jpg",
            "site/images/tivra-gallery-1.webp",
            "site/images/tivra-gallery-2.webp",
        ],
        "cereal-editorial": [
            "site/images/7_cereal-editorial.jpg",
            "site/images/2_creative-agency-mockup.jpg",
            "site/images/1_branding-mockup.jpg",
        ],
        "lumina-label": [
            "site/images/8_lumina-label.jpg",
            "site/images/3_stationery-mockup.jpg",
            "site/images/5_aura-packaging.jpg",
        ],
        "tattva": [
            "site/images/9_tattva.png",
            "site/images/1_branding-mockup.jpg",
            "site/images/2_creative-agency-mockup.jpg",
        ],
    }

    fallback_images = fallback_gallery.get(project.slug, [
        project.image_url,
        "site/images/portfolio-hero.webp",
        "site/images/services-hero.webp",
    ])
    gallery = project.gallery_image_list or fallback_images
    if project.image:
        image_name = project.image.name.rsplit("/", 1)[-1]
        gallery = [project.image_url] + [
            item for item in gallery
            if item.rsplit("/", 1)[-1] != image_name
        ][:3]

    context.update({
        "page_title": project.title,
        "project": project,
        "gallery_images": gallery,
        "project_services": project.provided_service_list,
        "related_projects": active_projects.exclude(pk=project.pk)[:3],
        "previous_project": active_projects.filter(order__lt=project.order).last(),
        "next_project": active_projects.filter(order__gt=project.order).first(),
    })
    return render(request, "website/portfolio_detail.html", context)


def blog(request):
    context = site_context()
    context.update({
        "page_title": "Blog",
        "posts": BlogPost.objects.filter(active=True, published=True, published_at__lte=timezone.now()),
    })
    return render(request, "website/blog.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, active=True, published=True)
    context = site_context()
    context.update({"page_title": post.title, "post": post})
    published_posts = BlogPost.objects.filter(active=True, published=True).exclude(pk=post.pk)
    context["previous_post"] = published_posts.filter(
        published_at__lt=post.published_at
    ).order_by("-published_at", "-id").first()
    context["next_post"] = published_posts.filter(
        published_at__gt=post.published_at
    ).order_by("published_at", "id").first()
    context["related_posts"] = published_posts[:3]
    return render(request, "website/blog_detail.html", context)


def contact(request):
    context = site_context()
    context["page_title"] = "Contact"
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        city = request.POST.get("city", "").strip()
        if not name or not email or not phone or not city:
            messages.error(request, "Please fill in your name, email, phone number and city.")
        else:
            ContactSubmission.objects.create(
                name=name,
                email=email,
                phone=phone,
                city=city,
            )
            url = (SiteSettings.objects.first().google_form_url if SiteSettings.objects.first() else "") or getattr(settings, "GOOGLE_FORM_URL", "")
            if url:
                data = {}
                mappings = {
                    "GOOGLE_FORM_ENTRY_NAME": name,
                    "GOOGLE_FORM_ENTRY_EMAIL": email,
                    "GOOGLE_FORM_ENTRY_PHONE": phone,
                    "GOOGLE_FORM_ENTRY_CITY": city,
                }
                for key, value in mappings.items():
                    entry = getattr(settings, key, "")
                    if entry:
                        data[entry] = value
                try:
                    requests.post(url, data=data, timeout=8)
                except requests.RequestException:
                    pass
            messages.success(request, "Thanks! Your enquiry has been received.")
            return redirect("contact")
    return render(request, "website/contact.html", context)
