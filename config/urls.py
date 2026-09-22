from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap, ServiceSitemap, PortfolioSitemap, BlogSitemap

from website import views

sitemaps = {"static": StaticViewSitemap, "services": ServiceSitemap, "portfolio": PortfolioSitemap, "blog": BlogSitemap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django-sitemap"),
    path("robots.txt", lambda request: __import__("django.http", fromlist=["HttpResponse"]).HttpResponse("User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n", content_type="text/plain"), name="robots"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolio/<slug:slug>/", views.portfolio_detail, name="portfolio_detail"),
    path("blog/", views.blog, name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("contact/", views.contact, name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
