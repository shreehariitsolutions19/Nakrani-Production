from django.db import migrations


def set_default_social_links(apps, schema_editor):
    SiteSettings = apps.get_model("website", "SiteSettings")
    site_settings = SiteSettings.objects.order_by("id").first()
    if site_settings is None:
        return

    defaults = {
        "facebook": "https://www.facebook.com/",
        "linkedin": "https://www.linkedin.com/",
        "instagram": "https://www.instagram.com/",
        "twitter": "https://x.com/",
    }
    changed = False
    for field, value in defaults.items():
        if not getattr(site_settings, field):
            setattr(site_settings, field, value)
            changed = True
    if changed:
        site_settings.save(update_fields=[*defaults, "updated_at"])


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0010_restore_testimonial_name"),
    ]

    operations = [
        migrations.RunPython(set_default_social_links, migrations.RunPython.noop),
    ]