from django.db import migrations


def restore_testimonial_name(apps, schema_editor):
    Testimonial = apps.get_model("website", "Testimonial")
    Testimonial.objects.filter(client_name="Hitul Nakrani").update(client_name="Ravi Patel")


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0009_update_testimonial_name"),
    ]

    operations = [
        migrations.RunPython(restore_testimonial_name, migrations.RunPython.noop),
    ]