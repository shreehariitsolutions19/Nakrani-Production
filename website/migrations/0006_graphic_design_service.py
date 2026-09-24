from django.db import migrations


def create_graphic_design_service(apps, schema_editor):
    Service = apps.get_model("website", "Service")
    Service.objects.get_or_create(
        slug="graphic-design",
        defaults={
            "title": "Graphic Design",
            "description": "Creative visual communication that makes your message clear, consistent and compelling.",
            "icon_class": "ri-brush-line",
            "features": "\n".join([
                "Campaign Design",
                "Marketing Collateral",
                "Brochures & Flyers",
                "Poster Design",
                "Presentation Design",
                "Visual Assets",
            ]),
            "process": "\n".join([
                "Discover",
                "Strategy",
                "Design",
                "Refine",
                "Deliver",
            ]),
            "order": 2,
            "active": True,
        },
    )


def remove_graphic_design_service(apps, schema_editor):
    Service = apps.get_model("website", "Service")
    Service.objects.filter(slug="graphic-design").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0005_contact_company_timeline"),
    ]

    operations = [
        migrations.RunPython(
            create_graphic_design_service,
            remove_graphic_design_service,
        ),
    ]
