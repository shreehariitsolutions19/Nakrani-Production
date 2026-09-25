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

Create a PostgreSQL database named `nakrani_production` in pgAdmin (or with
`CREATE DATABASE nakrani_production;`). Copy `.env.example` to `.env` and set
`POSTGRES_PASSWORD` to the password created for the PostgreSQL user. The local
PostgreSQL connection uses `127.0.0.1:5800` by default. If your provider supplies
a `DATABASE_URL`, that URL takes precedence over the local PostgreSQL settings.

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

## Exporting and importing website data

The current website content snapshot is stored in
`website/fixtures/website_data.json`. Refresh it from the configured database with:

```bash
python manage.py dumpdata website --indent 2 --output website/fixtures/website_data.json
```

After running migrations on another database, load that snapshot with:

```bash
python manage.py loaddata website/fixtures/website_data.json
```

## Important implementation note

The supplied reference is a captured preview/homepage rather than the private source repository of the Readdy site. Observable visual details and captured assets are reproduced directly where available; inner routes use the same reference design system rather than inventing a separate theme.
