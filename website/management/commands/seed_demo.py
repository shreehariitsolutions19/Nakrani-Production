from datetime import datetime
from pathlib import Path
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from website.models import BlogPost, PortfolioProject, Service, Testimonial


SERVICES = [
    {
        "title": "Branding & Identity",
        "slug": "branding-identity",
        "description": "Build a distinctive visual identity with logos, typography, colors, guidelines and brand systems.",
        "icon_class": "ri-palette-line",
        "features": "Logo Design\nColor System\nTypography\nBrand Guidelines\nVisual Language\nBrand Applications",
    },
    {
        "title": "Graphic Design",
        "slug": "graphic-design",
        "description": "Creative visual communication designed for campaigns, businesses and brands.",
        "icon_class": "ri-brush-line",
        "features": "Campaign Design\nMarketing Collateral\nBrochures & Flyers\nPoster Design\nPresentation Design\nVisual Assets",
    },
    {
        "title": "Print Design",
        "slug": "print-design",
        "description": "Professional brochures, flyers, posters, stationery, catalogs and print-ready marketing materials.",
        "icon_class": "ri-file-list-3-line",
        "features": "Brochures & Catalogs\nFlyers & Posters\nStationery\nEditorial Layouts\nPrint-ready Artwork",
    },
    {
        "title": "Packaging Design",
        "slug": "packaging-design",
        "description": "Packaging concepts that combine strong visual identity with practical communication.",
        "icon_class": "ri-box-3-line",
        "features": "Packaging Concepts\nProduct Labels\nStructural Design\nPrint Production\nPackaging Guidelines",
    },
    {
        "title": "Social Media Design",
        "slug": "social-media-design",
        "description": "Scroll-stopping social media creatives, campaign graphics and branded content.",
        "icon_class": "ri-share-line",
        "features": "Social Media Posts\nStory Templates\nCampaign Graphics\nBranded Content\nMotion-ready Assets",
    },
    {
        "title": "Digital Design",
        "slug": "digital-design",
        "description": "Modern digital visuals and creative assets designed for websites and online experiences.",
        "icon_class": "ri-computer-line",
        "features": "Web Interface Visuals\nDigital Campaigns\nApp UI Assets\nWeb Graphics\nArt Direction",
    },
]

PROCESS = "Discover\nStrategy\nDesign\nRefine\nDeliver"

PROJECTS = [
    {
        "title": "Tivra Brand",
        "slug": "tivra-brand",
        "category": "Branding & Identity",
        "description": "Tivra came to us as a growing studio with big ambition but a scattered visual presence. We built a complete identity system that gives the brand a confident, premium voice across every touchpoint — from the core mark to the finest print detail.",
        "design_details": "We leaned into warm copper tones against deep charcoal to create a sense of quiet confidence. The wordmark was refined for clarity while the supporting system stays flexible enough to scale across print, packaging and digital.",
        "provided_services": "Brand Strategy\nLogo & Identity System\nTypography & Colour\nStationery & Collateral",
        "challenge": "A growing studio with genuine ambition but a scattered visual presence across print, packaging and digital.",
        "solution": "A complete identity system covering the core mark, typography, colour and stationery.",
        "result": "A confident, premium voice that now reads consistently across every touchpoint.",
        "client": "Tivra",
        "year": 2025,
        "image": "6_tivra-brand.jpg",
        "gallery_images": "site/images/tivra-gallery-1.webp\nsite/images/tivra-gallery-2.webp\nsite/images/tivra-gallery-3.webp",
        "featured": True,
    },
    {
        "title": "TATTVA",
        "slug": "tattva",
        "category": "Branding & Identity",
        "description": "TATTVA needed an identity that felt rooted and timeless while still feeling modern. We created a refined visual language built around balance, warmth and clarity that carries naturally into signage and print.",
        "design_details": "The direction pairs a strong geometric mark with generous whitespace and a restrained copper accent, letting the brand feel considered rather than loud.",
        "provided_services": "Brand Identity\nLogo Design\nSignage & Wayfinding\nPrint Collateral",
        "challenge": "An identity that needed to feel rooted and timeless while still reading as modern.",
        "solution": "A refined visual language carrying naturally into signage, wayfinding and print collateral.",
        "result": "A brand that feels considered rather than loud, equally at home in physical space.",
        "client": "Tattva",
        "year": 2025,
        "image": "9_tattva.png",
        "gallery_images": "site/images/1_branding-mockup.jpg\nsite/images/2_creative-agency-mockup.jpg",
        "featured": False,
    },
    {
        "title": "MOON Cosmetics",
        "slug": "moon-cosmetics",
        "category": "Packaging & Branding",
        "description": "MOON Cosmetics wanted packaging that would stand out on a crowded shelf while still feeling understated. We designed a full range system that feels luxurious, tactile and unmistakably premium.",
        "design_details": "Matte charcoal surfaces meet delicate copper foil detailing, creating a quiet luxury that rewards a closer look.",
        "provided_services": "Packaging Design\nProduct Label System\nBrand Identity\nArt Direction",
        "challenge": "Standing out on a crowded shelf while still feeling understated and premium.",
        "solution": "A full range packaging system with one consistent label and surface language.",
        "result": "A luxurious, tactile range that feels collectible and unmistakably premium.",
        "client": "MOON Cosmetics",
        "year": 2024,
        "image": "4_moon-cosmetics.jpg",
        "gallery_images": "site/images/3_stationery-mockup.jpg\nsite/images/2_creative-agency-mockup.jpg",
        "featured": False,
    },
    {
        "title": "Aura Packaging",
        "slug": "aura-packaging",
        "category": "Packaging Design",
        "description": "Aura needed a packaging system that balanced practicality with a genuinely premium feel. We developed structural concepts and surface treatments that make every unboxing feel intentional.",
        "design_details": "The system uses a warm copper identity over deep charcoal, with clean typographic hierarchy so each product reads instantly.",
        "provided_services": "Packaging Concepts\nStructural Design\nPrint Production\nBrand Guidelines",
        "challenge": "Balancing practical production with a genuinely premium unboxing feel.",
        "solution": "A warm copper identity over deep charcoal with a clean typographic hierarchy.",
        "result": "Every unboxing feels intentional and each product reads instantly on shelf.",
        "client": "Aura",
        "year": 2024,
        "image": "5_aura-packaging.jpg",
        "gallery_images": "site/images/3_stationery-mockup.jpg\nsite/images/1_branding-mockup.jpg",
        "featured": False,
    },
    {
        "title": "Lumina Label",
        "slug": "lumina-label",
        "category": "Label & Packaging",
        "description": "Lumina asked for a label system that would elevate a small-batch product into something that feels collectible. The result is a family of labels that share a clear visual signature.",
        "design_details": "Fine copper linework and restrained typography give the labels a crafted, almost editorial quality.",
        "provided_services": "Label Design\nPackaging System\nPrint Production\nArt Direction",
        "challenge": "Elevating a small-batch product into something that feels collectible.",
        "solution": "A family of labels sharing one clear visual signature across the range.",
        "result": "A crafted label system that gives the product quiet presence on shelf.",
        "client": "Lumina",
        "year": 2024,
        "image": "8_lumina-label.jpg",
        "gallery_images": "site/images/3_stationery-mockup.jpg\nsite/images/5_aura-packaging.jpg",
        "featured": False,
    },
    {
        "title": "Cereal Editorial",
        "slug": "cereal-editorial",
        "category": "Print & Editorial",
        "description": "Cereal wanted a publication with a strong editorial voice. We built a grid, type system and print identity that lets the content breathe while staying unmistakably designed.",
        "design_details": "Confident typographic hierarchy and a strict editorial grid are softened with warm copper details throughout.",
        "provided_services": "Editorial Design\nLayout System\nTypography Direction\nPrint Production",
        "challenge": "Finding a strong editorial voice that lets the content breathe.",
        "solution": "A publication identity with a repeatable grid, type system and print language.",
        "result": "A designed, readable publication that stays unmistakably on-brand.",
        "client": "Cereal",
        "year": 2024,
        "image": "7_cereal-editorial.jpg",
        "gallery_images": "site/images/2_creative-agency-mockup.jpg\nsite/images/1_branding-mockup.jpg",
        "featured": False,
    },
    {
        "title": "Verta Mark",
        "slug": "verta-mark",
        "category": "Logo Identity",
        "description": "Verta needed a single distinctive mark that could carry a whole brand. We crafted a monogram emblem that stays elegant at any scale and feels premium in foil.",
        "design_details": "The mark balances geometric precision with a hand-finished foil treatment for depth and warmth.",
        "provided_services": "Logo Design\nMonogram & Emblem\nFoil & Finishing\nBrand Collateral",
        "challenge": "Creating a single distinctive mark that could carry an entire brand.",
        "solution": "A monogram emblem that stays elegant at any scale, with supporting collateral.",
        "result": "A premium mark that holds its own from favicon to signage.",
        "client": "Verta",
        "year": 2025,
        "image": "",
        "gallery_images": "",
        "featured": False,
    },
    {
        "title": "Nova Identity",
        "slug": "nova-identity",
        "category": "Logo & Identity",
        "description": "Nova needed a flexible identity that could grow with the business. We designed a modular mark and a supporting system that stays consistent across every medium.",
        "design_details": "A clean geometric mark paired with warm copper accents keeps the brand modern without feeling cold.",
        "provided_services": "Logo Design\nIdentity System\nStationery Design\nBrand Guidelines",
        "challenge": "Building an identity flexible enough to grow with the business.",
        "solution": "A modular mark and supporting system spanning stationery and signage.",
        "result": "A consistent identity that scales effortlessly across every medium.",
        "client": "Nova",
        "year": 2025,
        "image": "",
        "gallery_images": "",
        "featured": False,
    },
    {
        "title": "Pulse Social",
        "slug": "pulse-social",
        "category": "Social Media Design",
        "description": "Pulse wanted scroll-stopping content with a consistent look. We built a flexible template system that keeps every post on-brand while staying fresh.",
        "design_details": "Bold type and a warm copper accent system make each post recognisable at a glance in a crowded feed.",
        "provided_services": "Social Media Design\nContent Templates\nCampaign Graphics\nMotion-ready Assets",
        "challenge": "Staying consistent and recognisable inside a fast, crowded feed.",
        "solution": "A flexible template system covering posts, stories and campaign graphics.",
        "result": "Content that stays on-brand while still feeling fresh week to week.",
        "client": "Pulse",
        "year": 2025,
        "image": "",
        "gallery_images": "",
        "featured": False,
    },
    {
        "title": "Orbit Digital",
        "slug": "orbit-digital",
        "category": "Digital Design",
        "description": "Orbit needed a digital presence as refined as their product. We designed interface visuals and creative assets that feel consistent with their brand across web and app.",
        "design_details": "Clean layouts with warm copper highlights create a digital experience that feels premium but effortless to use.",
        "provided_services": "Digital Design\nWeb Interface Visuals\nApp UI Assets\nArt Direction",
        "challenge": "A digital presence that needed to feel as refined as the product itself.",
        "solution": "Interface visuals, app assets and campaign graphics sharing one art direction.",
        "result": "A digital experience that feels consistent across web and app.",
        "client": "Orbit",
        "year": 2025,
        "image": "",
        "gallery_images": "",
        "featured": False,
    },
]

BLOG_POSTS = [
    {
        "title": "Why Strong Visual Identity Matters for Modern Brands",
        "slug": "why-strong-visual-identity-matters",
        "category": "Branding",
        "excerpt": "A strong visual identity is more than a logo — it is the system that makes a brand instantly recognisable, trustworthy and impossible to forget.",
        "published_at": (2026, 9, 12),
        "image": "1_branding-mockup.jpg",
        "content": """In a market where attention lasts a fraction of a second, a brand is judged long before it is understood. Long before a customer reads a single word, they have already formed an impression from colour, type, spacing and form. That impression is your visual identity at work.

A strong identity is not a single logo file. It is a connected system — a mark, a palette, a type hierarchy and a set of rules — that behaves consistently across packaging, print, digital and social. The stronger the system, the more recognisable the brand becomes with every exposure.

Consistency builds trust

Repetition is how memory forms. When a brand shows up in the same considered way across every touchpoint, audiences start to trust it without being able to explain why. Inconsistency, on the other hand, reads as uncertainty — and uncertainty rarely converts.

Great visual identity does not just make a brand look good. It makes a brand feel inevitable.

The most memorable brands treat identity as infrastructure, not decoration. It is the foundation that lets everything else — campaigns, packaging, product, digital — scale without losing its soul.""",
    },
    {
        "title": "How to Build a Memorable Brand Identity",
        "slug": "how-to-build-a-memorable-brand-identity",
        "category": "Branding",
        "excerpt": "From positioning to palette — the practical foundations that turn a business into a brand people remember.",
        "published_at": (2026, 8, 28),
        "image": "6_tivra-brand.jpg",
        "content": """Every memorable brand identity starts with clarity before craft. Before a single mark is drawn, we define what the brand stands for, who it speaks to, and what it should feel like in the mind of the audience.

Start with positioning

Positioning gives the visual work a direction. It answers the questions that colour and type must later express: are we warm or sharp, premium or approachable, bold or understated?

Only then do we move into the mark, the type system and the palette — each decision checked against the positioning so the identity feels inevitable rather than arbitrary.

A brand identity is a decision system disguised as a visual style.""",
    },
    {
        "title": "The Psychology Behind Effective Logo Design",
        "slug": "psychology-behind-effective-logo-design",
        "category": "Graphic Design",
        "excerpt": "Why the simplest marks are often the strongest, and how shape, balance and negative space shape perception.",
        "published_at": (2026, 8, 14),
        "image": "1_branding-mockup.jpg",
        "content": """A logo is read in milliseconds, and the brain makes its judgement before the conscious mind catches up. That is why the strongest marks rely on shape and balance rather than detail.

Simplicity is not the absence of thinking

A simple mark is the result of relentless reduction. Every unnecessary line is removed until only the essential idea remains — and that essential idea is what people remember.

Negative space, proportion and optical balance do the quiet work. When they are right, the logo feels stable and confident at any size, from a favicon to a storefront.""",
    },
    {
        "title": "Packaging Design That Gets Noticed",
        "slug": "packaging-design-that-gets-noticed",
        "category": "Packaging",
        "excerpt": "Packaging is the first physical touchpoint of a brand. Here is how to make it work on a crowded shelf.",
        "published_at": (2026, 7, 30),
        "image": "5_aura-packaging.jpg",
        "content": """Packaging has a hard job: it must attract, inform and reassure — often within a few seconds and a single glance. On a crowded shelf, clarity beats decoration every time.

Design for the three-foot and the three-inch view

A great pack reads instantly from across the aisle and rewards a closer look in the hand. Hierarchy, contrast and material finish all contribute to that double reading.

Packaging is the only medium your customer holds in their hands before they buy.""",
    },
    {
        "title": "Designing Social Media Content That Stands Out",
        "slug": "social-media-content-that-stands-out",
        "category": "Social Media",
        "excerpt": "A consistent template system can keep every post on-brand while still feeling fresh in a fast feed.",
        "published_at": (2026, 7, 16),
        "image": "2_creative-agency-mockup.jpg",
        "content": """Social feeds move fast, and audiences scroll faster. The brands that stand out are not always the loudest — they are the most consistent and recognisable.

Build a system, not one-offs

A flexible template system keeps posts on-brand without making them repetitive. Clear type, a confident palette and a repeatable grid let content stay fresh while remaining unmistakably yours.

Recognition is the goal. When someone can identify your brand from a thumbnail alone, the design is doing its job.""",
    },
    {
        "title": "Why Typography Matters in Branding",
        "slug": "why-typography-matters-in-branding",
        "category": "Branding",
        "excerpt": "Type carries tone before words do. The right typeface can make a brand feel premium, bold or quietly confident.",
        "published_at": (2026, 6, 28),
        "image": "3_stationery-mockup.jpg",
        "content": """Typography is the voice of a brand made visible. Before a reader processes a single word, the shape and weight of the letterforms have already set the tone.

Type does the emotional work

A geometric sans speaks differently than a high-contrast serif. Choosing type is choosing a personality — and that choice must align with the positioning of the brand.

Scale, spacing and hierarchy then turn that personality into a system that stays legible and considered across every format.""",
    },
    {
        "title": "From Concept to Creative: Our Design Process",
        "slug": "from-concept-to-creative-design-process",
        "category": "Creative Process",
        "excerpt": "A look inside how we move from a first conversation to finished, production-ready creative work.",
        "published_at": (2026, 6, 10),
        "image": "2_creative-agency-mockup.jpg",
        "content": """Good design rarely arrives fully formed. It is the result of a deliberate process that moves from understanding to exploring, refining and finally delivering.

Discover, define, design, deliver

We begin by listening — understanding the brand, the audience and the objective. From there we define a clear creative direction that gives every later decision a purpose.

With the direction set, we design and refine until the work is resolved, then prepare polished, production-ready assets that hold up in the real world.

A clear process is what turns creativity into something reliable.""",
    },
    {
        "title": "Print Design in a Digital-First World",
        "slug": "print-design-in-a-digital-first-world",
        "category": "Print",
        "excerpt": "Print is not disappearing — it is becoming a premium, tactile counterpoint to the screen.",
        "published_at": (2026, 5, 22),
        "image": "7_cereal-editorial.jpg",
        "content": """In a world saturated with screens, print has become a rare and tactile signal of quality. Paper, finish and weight communicate in ways a pixel cannot.

Print rewards the senses

A well-made brochure or catalogue asks to be held and kept. That physical presence creates an intimacy and permanence that digital rarely achieves.

The strongest brands use print deliberately — as a considered counterpoint to their digital presence, not a replacement for it.""",
    },
    {
        "title": "Building Consistency Across Every Brand Touchpoint",
        "slug": "building-consistency-across-every-brand-touchpoint",
        "category": "Branding",
        "excerpt": "Consistency is what turns a set of assets into a brand. Here is how to keep every touchpoint aligned.",
        "published_at": (2026, 5, 6),
        "image": "6_tivra-brand.jpg",
        "content": """A brand is only as strong as its least considered touchpoint. One off-brand post or mismatched label quietly erodes the trust the rest of the identity has built.

Guidelines are a tool, not a rulebook

Clear guidelines give a team the confidence to apply the identity correctly — and the freedom to stay creative within it. They are there to enable, not restrict.

Consistency is not repetition. It is recognition.""",
    },
]


class Command(BaseCommand):
    help = "Populate the database with the services, portfolio and journal data from the preview."

    def copy_demo_image(self, filename, folder):
        if not filename:
            return ""
        source = Path(settings.BASE_DIR) / "website" / "static" / "site" / "images" / filename
        if not source.exists():
            self.stderr.write(self.style.WARNING(f"Preview image is not available locally: {filename}"))
            return ""
        destination_dir = Path(settings.MEDIA_ROOT) / folder
        destination_dir.mkdir(parents=True, exist_ok=True)
        destination = destination_dir / filename
        if not destination.exists():
            shutil.copy2(source, destination)
        return f"{folder}/{filename}"

    def handle(self, *args, **options):
        for index, service_data in enumerate(SERVICES, start=1):
            Service.objects.update_or_create(
                slug=service_data["slug"],
                defaults={
                    **service_data,
                    "process": PROCESS,
                    "order": index,
                    "active": True,
                },
            )

        for index, project_data in enumerate(PROJECTS, start=1):
            data = project_data.copy()
            data["image"] = self.copy_demo_image(data.pop("image"), "portfolio")
            PortfolioProject.objects.update_or_create(
                slug=data.pop("slug"),
                defaults={
                    **data,
                    "order": index,
                    "active": True,
                },
            )

        Testimonial.objects.update_or_create(
            client_name="Ravi Patel",
            defaults={
                "role": "Founder",
                "company": "Urban Style",
                "quote": "Nakrani Production understood our vision perfectly and delivered a brand identity that truly represents our business. Highly professional and creative team!",
                "rating": 5,
                "active": True,
                "photo": self.copy_demo_image("10_ravi-patel.jpg", "testimonials"),
            },
        )

        for post_data in BLOG_POSTS:
            data = post_data.copy()
            year, month, day = data.pop("published_at")
            data["published_at"] = timezone.make_aware(datetime(year, month, day, 9, 0))
            data["cover_image"] = self.copy_demo_image(data.pop("image"), "blog")
            BlogPost.objects.update_or_create(
                slug=data.pop("slug"),
                defaults={
                    **data,
                    "author": "Nakrani Studio",
                    "read_time": 6,
                    "published": True,
                    "active": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Preview content is ready: 6 services, 10 portfolio projects, "
                "1 testimonial and 9 journal articles."
            )
        )
