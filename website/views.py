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
    })
    return render(request, "website/portfolio.html", context)


def portfolio_detail(request, slug):
    project = get_object_or_404(PortfolioProject, slug=slug, active=True)
    context = site_context()
    context.update({
        "page_title": project.title,
        "project": project,
        "related_projects": PortfolioProject.objects.filter(active=True).exclude(pk=project.pk)[:3],
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
    context["related_posts"] = BlogPost.objects.filter(active=True, published=True).exclude(pk=post.pk)[:3]
    return render(request, "website/blog_detail.html", context)


def contact(request):
    context = site_context()
    context["page_title"] = "Contact"
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        project_type = request.POST.get("project_type", "").strip()
        budget = request.POST.get("budget", "").strip()
        message = request.POST.get("message", "").strip()
        if not name or not email or not message:
            messages.error(request, "Please fill in your name, email and message.")
        else:
            submission = ContactSubmission.objects.create(
                name=name, email=email, phone=phone, project_type=project_type,
                budget=budget, message=message,
            )
            url = (SiteSettings.objects.first().google_form_url if SiteSettings.objects.first() else "") or getattr(settings, "GOOGLE_FORM_URL", "")
            if url:
                data = {}
                mappings = {
                    "GOOGLE_FORM_ENTRY_NAME": name,
                    "GOOGLE_FORM_ENTRY_EMAIL": email,
                    "GOOGLE_FORM_ENTRY_PHONE": phone,
                    "GOOGLE_FORM_ENTRY_PROJECT_TYPE": project_type,
                    "GOOGLE_FORM_ENTRY_BUDGET": budget,
                    "GOOGLE_FORM_ENTRY_MESSAGE": message,
                }
                for key, value in mappings.items():
                    entry = getattr(settings, key, "")
                    if entry:
                        data[entry] = value
                try:
                    response = requests.post(url, data=data, timeout=8)
                    if response.ok:
                        submission.google_synced = True
                        submission.save(update_fields=["google_synced"])
                except requests.RequestException:
                    pass
            messages.success(request, "Thanks! Your enquiry has been received.")
            return redirect("contact")
    return render(request, "website/contact.html", context)
