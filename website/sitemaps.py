from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost, PortfolioProject, Service

class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'
    def items(self): return ['home','about','services','portfolio','blog','contact']
    def location(self, item): return reverse(item)

class ServiceSitemap(Sitemap):
    def items(self): return Service.objects.filter(active=True)
    def location(self, obj): return reverse('service_detail', kwargs={'slug': obj.slug})

class PortfolioSitemap(Sitemap):
    def items(self): return PortfolioProject.objects.filter(active=True)
    def location(self, obj): return reverse('portfolio_detail', kwargs={'slug': obj.slug})

class BlogSitemap(Sitemap):
    def items(self): return BlogPost.objects.filter(active=True)
    def location(self, obj): return reverse('blog_detail', kwargs={'slug': obj.slug})
