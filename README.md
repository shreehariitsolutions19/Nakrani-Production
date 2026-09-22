# Nakrani Production — Complete Django Reference Build

This project is a Django implementation of the supplied Readdy preview. The preview is treated as the visual source of truth; the Django layer adds real routes, database-driven content, Admin editing, contact storage and Google Forms integration.

Reference preview:
https://readdy.cc/preview/cc1ae3a4-db43-4b1a-be04-464564cf66b3/11278772

## Included

- Reference-matched Home page using the captured visual assets
- Shared reference header/navigation/footer on every route
- About, Services, Service Detail, Portfolio, Portfolio Detail, Blog, Blog Detail and Contact pages
- Django ORM models, migrations and Admin
- Demo images extracted from the supplied reference capture
- `seed_demo` command to populate content and copy demo images into `media/`
- Contact submissions saved to the database
- Optional Google Forms forwarding with `.env` entry mappings
- Responsive mobile navigation
- Scroll reveal and subtle mouse/parallax interactions
- SEO metadata, sitemap and robots.txt
- Custom 404/500 pages using the same design system

## Windows setup

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

Website: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

## Google Forms

Copy `.env.example` to `.env` and fill the Google Form URL plus the `entry.xxxxx` field IDs. The Django submission is saved first. Google forwarding is best-effort and never blocks a successful website submission.

## Editing content

Use Django Admin to replace services, portfolio images, testimonials, blog posts, site contact details and other database content. The demo content is intentionally replaceable.

## Important implementation note

The supplied reference is a captured preview/homepage rather than the private source repository of the Readdy site. Observable visual details and captured assets are reproduced directly where available; inner routes use the same reference design system rather than inventing a separate theme.
