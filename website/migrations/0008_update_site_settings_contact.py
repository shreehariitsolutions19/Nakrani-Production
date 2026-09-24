from django.db import migrations


def update_site_settings(apps, schema_editor):
    SiteSettings = apps.get_model("website", "SiteSettings")
    site_settings = SiteSettings.objects.order_by("id").first()
    if site_settings is None:
        SiteSettings.objects.create(
            brand_name="Nakrani Production",
            owner_name="Hitul Nakrani",
            phone="+91 70162 28333",
            email="Design.Hitul@gmail.com",
            city="Visnagar, Mehsana, Gujarat, India",
            address="Visnagar, Mehsana, Gujarat, India",
        )
        return

    site_settings.owner_name = "Hitul Nakrani"
    site_settings.phone = "+91 70162 28333"
    site_settings.email = "Design.Hitul@gmail.com"
    site_settings.city = "Visnagar, Mehsana, Gujarat, India"
    site_settings.address = "Visnagar, Mehsana, Gujarat, India"
    site_settings.save(update_fields=["owner_name", "phone", "email", "city", "address", "updated_at"])


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0007_sitesettings_owner_name_alter_sitesettings_city_and_more"),
    ]

    operations = [
        migrations.RunPython(update_site_settings, migrations.RunPython.noop),
    ]