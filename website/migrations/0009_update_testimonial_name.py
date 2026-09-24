from django.db import migrations


def update_testimonial_name(apps, schema_editor):
    Testimonial = apps.get_model("website", "Testimonial")
    Testimonial.objects.filter(client_name="Ravi Patel").update(client_name="Hitul Nakrani")


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0008_update_site_settings_contact"),
    ]

    operations = [
        migrations.RunPython(update_testimonial_name, migrations.RunPython.noop),
    ]