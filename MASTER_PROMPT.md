# MASTER PROMPT — BUILD COMPLETE DJANGO WEBSITE FROM REFERENCE

You are an expert UI/UX designer, frontend developer, Django developer, animation engineer, and full-stack architect.

I want you to build a COMPLETE, PROFESSIONAL, PRODUCTION-READY graphic design agency website using Django.

## 1. SINGLE SOURCE OF VISUAL TRUTH

Use ONLY this reference preview to study the website design, layout, typography, colors, spacing, animations, interactions, responsive behavior, visual hierarchy, and overall design language:

REFERENCE PREVIEW:
[https://readdy.cc/preview/cc1ae3a4-db43-4b1a-be04-464564cf66b3/11278772](https://readdy.cc/preview/cc1ae3a4-db43-4b1a-be04-464564cf66b3/11278772)

IMPORTANT:

- Do not redesign the website.
- Do not create a generic graphic-design-agency template.
- Do not replace the visual style with your own design.
- Reproduce the reference as closely as technically possible.
- Study the complete preview carefully before writing code.
- Match desktop AND mobile behavior.
- Match typography, font weights, font sizes, line heights, spacing, border radius, shadows, cards, buttons, sections, navigation, animations and transitions.
- Preserve the premium/minimal creative-agency aesthetic.
- If something cannot be determined exactly from the preview, choose the closest implementation consistent with the reference instead of inventing a completely different design.

The final website should feel like the same website, but implemented properly in Django with a database and admin panel.

---

# 2. TECHNOLOGY STACK

Use:

Backend:

- Python
- Django 5.x
- Django ORM
- SQLite for development
- PostgreSQL-compatible architecture for production

Frontend:

- HTML5
- CSS3
- Vanilla JavaScript
- Bootstrap/Tailwind ONLY if necessary
- Prefer custom CSS when required to achieve visual accuracy

Do NOT use React, Next.js, Vue, Angular or another frontend framework.

Use Django Templates.

Required packages should be placed in:

requirements.txt

Use environment variables through:

.env

Provide:

.env.example

---

# 3. PROJECT ARCHITECTURE

Create a clean Django project:

project/
│
├── manage.py
│
├── config/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── website/
│ ├── migrations/
│ ├── management/
│ │ └── commands/
│ │ └── seed_demo.py
│ ├── templates/
│ │ └── website/
│ ├── static/
│ │ ├── css/
│ │ ├── js/
│ │ └── images/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ ├── forms.py
│ └── apps.py
│
├── media/
├── staticfiles/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

IMPORTANT:

Do NOT name the Django app "site".

Use:

website

This avoids conflict with Python's built-in "site" module.

---

# 4. COMPLETE PAGE STRUCTURE

Build ALL of the following pages.

## PAGE 1 — HOME

URL:

/

Recreate the reference homepage as accurately as possible.

Include:

- Header
- Navigation
- Logo/brand
- Hero section
- Hero heading
- Hero description
- Hero CTA buttons
- Floating visual cards
- Hero mouse/parallax interaction
- Services preview
- Portfolio preview
- About preview
- Testimonial
- CTA section
- Footer

The homepage must visually match the reference.

---

# 5. ABOUT PAGE

URL:

/about/

Create a complete About page using the SAME design system as the reference.

Do not make it look like a generic About page.

Include:

### Hero

Large creative heading.

### Introduction

Agency/company introduction.

### Story

Company story and creative philosophy.

### Values

Display several company values as premium cards.

Example:

- Creativity
- Strategy
- Quality
- Innovation

### Process

Show the design/project process:

01 — Discover
02 — Strategy
03 — Design
04 — Refine
05 — Deliver

### Why Choose Us

Creative agency strengths.

### Testimonial

Use the same visual language as the homepage testimonial.

### CTA

"Let's work together"

Button:

"Start a Project"

---

# 6. SERVICES PAGE

URL:

/services/

Services MUST come from Django database.

Create:

Service model.

Fields:

- title
- slug
- description
- icon
- image
- order
- active
- created_at
- updated_at

Display services as premium cards.

Initial DEMO services:

1. Branding & Identity
2. Web Design
3. Print Design
4. Social Media Design

Each service should have:

- Icon
- Title
- Description
- Hover effect
- Animation
- CTA

Add a service-detail page:

/services//

The service detail page should include:

- Hero
- Service description
- Features
- Process
- Related portfolio
- CTA

---

# 7. PORTFOLIO PAGE

URL:

/portfolio/

Portfolio must be fully database-driven.

Create:

PortfolioProject model.

Fields:

- title
- slug
- category
- image
- description
- client
- year
- featured
- order
- active
- created_at
- updated_at

Demo projects:

- MOON Cosmetics
- Aura Packaging
- Tivra Brand
- Cereal Editorial
- Lumina Label
- TATTVA

Use high-quality placeholder/demo images if actual images are unavailable.

IMPORTANT:

Images must be replaceable from Django Admin.

Portfolio page should include:

- Page hero
- Category filters
- Project grid
- Hover animations
- Image transitions
- Project cards
- CTA

Create project detail page:

/portfolio//

Include:

- Large project image
- Project title
- Category
- Client
- Year
- Description
- Design details
- Related projects
- CTA

---

# 8. BLOG PAGE

URL:

/blog/

Create a fully dynamic blog system.

Create:

BlogPost model.

Fields:

- title
- slug
- excerpt
- content
- featured_image
- author
- category
- published
- published_at
- created_at
- updated_at

Blog listing:

- Featured article
- Blog cards
- Category
- Date
- Read More

Blog detail:

/blog//

Include:

- Title
- Featured image
- Author
- Date
- Category
- Full content
- Related posts
- CTA

---

# 9. CONTACT PAGE

URL:

/contact/

Create a premium contact page matching the reference design.

Include:

- Heading
- Introduction
- Contact information
- Email
- Phone
- Location
- Contact form

Form fields:

- Name
- Email
- Phone
- Project Type
- Budget
- Message

Create:

ContactSubmission model.

Fields:

- name
- email
- phone
- project_type
- budget
- message
- created_at
- status
- source
- google_synced

Admin must be able to view all submissions.

---

# 10. GOOGLE FORM INTEGRATION

The contact system must support Google Forms.

Use environment variables:

GOOGLE_FORM_URL=
GOOGLE_FORM_ENTRY_NAME=
GOOGLE_FORM_ENTRY_EMAIL=
GOOGLE_FORM_ENTRY_PHONE=
GOOGLE_FORM_ENTRY_PROJECT_TYPE=
GOOGLE_FORM_ENTRY_BUDGET=
GOOGLE_FORM_ENTRY_MESSAGE=

When a visitor submits the Django contact form:

1. Validate the form.
2. Save submission to Django database.
3. If Google Form configuration exists, submit data to Google Form.
4. Mark google_synced=True when successful.
5. Do not fail the user's submission if Google Forms is temporarily unavailable.
6. Show a professional success message.

---

# 11. SITE SETTINGS

Create:

SiteSettings model.

Fields:

- brand_name
- tagline
- logo
- favicon
- email
- phone
- address
- instagram
- linkedin
- facebook
- twitter
- google_form_url
- meta_title
- meta_description
- updated_at

Only one active SiteSettings record should be used.

All global website information should be editable through Admin.

---

# 12. TESTIMONIALS

Create:

Testimonial model.

Fields:

- client_name
- role
- company
- photo
- quote
- rating
- active
- created_at

Homepage should display testimonials dynamically.

---

# 13. DJANGO ADMIN

Create a professional Django Admin experience.

Admin must allow management of:

- Site Settings
- Services
- Portfolio Projects
- Testimonials
- Blog Posts
- Contact Submissions

Add:

- Search
- Filters
- Ordering
- Slugs
- Image previews
- Status fields
- Featured filters
- Active/inactive filters

Contact submissions should be easy to review.

---

# 14. NAVIGATION

Use:

Home
About
Services
Portfolio
Blog
Contact
Let's Talk

Navigation must work correctly.

Do NOT use hardcoded broken links.

Use Django:

{% url %}

for internal navigation.

---

# 15. RESPONSIVE DESIGN

The website must work properly on:

- Desktop
- Laptop
- Tablet
- Mobile

Breakpoints should be carefully implemented.

Mobile navigation should become a hamburger menu.

Ensure:

- No horizontal overflow
- Images scale correctly
- Typography adapts
- Buttons remain usable
- Cards stack correctly
- Navigation works
- Animations remain smooth

---

# 16. ANIMATIONS & INTERACTIONS

This is VERY IMPORTANT.

Recreate observable interactions from the reference.

Implement:

### Hero floating-card movement

Use JavaScript mouse movement/parallax.

Cards should subtly move based on cursor position.

Do NOT make the effect excessive.

### Scroll reveal

Sections/cards should animate into view.

Use:

IntersectionObserver

where appropriate.

### Hover animations

Implement smooth hover states for:

- Buttons
- Service cards
- Portfolio cards
- Navigation links
- Images
- CTA elements

### Page transitions

Use subtle transitions where appropriate.

### Mobile

Disable/reduce mouse-dependent effects on touch devices.

---

# 17. TYPOGRAPHY

Typography is extremely important.

Study the reference and reproduce:

- Font family
- Font weights
- Heading sizes
- Body sizes
- Letter spacing
- Line height
- Button typography
- Navigation typography

Do not arbitrarily choose another font.

If the reference uses an available web font, load the closest matching font correctly.

Create CSS typography variables.

---

# 18. COLORS

Extract the visual color system from the reference.

Use CSS variables:

\:root {
\--color-background:
\--color-text:
\--color-muted:
\--color-primary:
\--color-secondary:
\--color-border:
\--color-accent:
}

Do not introduce unrelated colors.

---

# 19. SPACING & LAYOUT

Match the reference carefully.

Pay attention to:

- Container width
- Section spacing
- Hero height
- Card gaps
- Grid columns
- Border radius
- Padding
- Margins
- Header height
- Footer spacing

Do not compress the design unnecessarily.

---

# 20. FOOTER

Create a complete footer.

Include:

Brand
Quick Links
Services
Support
Contact
Social links
Copyright

Footer content must come from SiteSettings wherever possible.

---

# 21. SEO

Implement:

- Dynamic page title
- Meta description
- Open Graph tags
- Twitter card tags
- Canonical URL
- Semantic HTML
- Proper H1/H2/H3 structure
- Alt text for images
- robots.txt
- sitemap.xml

Create Django sitemap support.

---

# 22. SECURITY

Follow Django security best practices.

Use:

- CSRF protection
- Secure form validation
- Environment variables for secrets
- No passwords/API keys in source code
- Proper DEBUG handling
- ALLOWED_HOSTS from environment
- Secure production settings

---

# 23. PERFORMANCE

Optimize:

- Images
- CSS
- JavaScript
- Lazy loading
- Font loading
- Database queries
- Static files

Avoid unnecessary JavaScript libraries.

---

# 24. DEMO DATA

The project MUST work immediately after setup.

Create:

seed_demo

Django management command.

Command:

python manage.py seed_demo

It should create demo:

- Site Settings
- Services
- Portfolio projects
- Testimonials
- Blog posts

Use safe placeholder images or locally available assets.

The demo data must NOT prevent me from replacing everything later.

---

# 25. DATABASE

Create proper migrations.

After fresh installation these commands must work:

python manage.py makemigrations
python manage.py migrate
python manage.py seed_demo

---

# 26. ADMIN ACCOUNT

Document:

python manage.py createsuperuser

in README.

---

# 27. RUN COMMANDS

README must contain exact Windows instructions:

python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py migrate

python manage.py seed_demo

python manage.py createsuperuser

python manage.py runserver

Website:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Admin:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

# 28. ERROR HANDLING

Create:

404 page
500 page

They must use the same design language as the website.

---

# 29. CODE QUALITY

Write clean maintainable code.

Do not place the entire website inside one massive HTML file if it can be properly templated.

Use:

base.html

header.html

footer.html

home.html

about.html

services.html

service_detail.html

portfolio.html

portfolio_detail.html

blog.html

blog_detail.html

contact.html

404.html

500.html

Use template inheritance.

---

# 30. IMPORTANT — DO NOT LOSE THE REFERENCE DESIGN

The most important requirement is:

VISUAL FIDELITY > PERSONAL DESIGN OPINION.

Do not:

- Modernize it unnecessarily
- Change the layout
- Change colors randomly
- Change typography randomly
- Remove animations
- Add unrelated sections
- Add excessive gradients
- Add excessive shadows
- Add unrelated icons
- Turn it into a generic Bootstrap website

The reference should remain the design authority.

---

# 31. FINAL QUALITY CHECK

Before considering the project complete, test:

1. Homepage loads.
2. About loads.
3. Services loads.
4. Service detail loads.
5. Portfolio loads.
6. Portfolio detail loads.
7. Blog loads.
8. Blog detail loads.
9. Contact loads.
10. Contact form submits.
11. Contact data saves to database.
12. Google Form integration works when configured.
13. Admin login works.
14. All models appear in Admin.
15. Images can be uploaded.
16. Demo data loads.
17. Mobile navigation works.
18. Desktop layout works.
19. Animations work.
20. Mouse/parallax interaction works.
21. No broken internal links.
22. No console errors.
23. No Django URL errors.
24. No template errors.
25. No horizontal overflow.
26. 404 works.
27. 500 works.

---

# 32. VISUAL QA

After implementation, run the Django server and inspect every page.

Compare the implementation against the reference preview:

[https://readdy.cc/preview/cc1ae3a4-db43-4b1a-be04-464564cf66b3/11278772](https://readdy.cc/preview/cc1ae3a4-db43-4b1a-be04-464564cf66b3/11278772)

Check:

- Header position
- Hero composition
- Typography
- Font weights
- Section spacing
- Cards
- Images
- Buttons
- Hover effects
- Animations
- Floating cards
- Footer
- Mobile responsiveness

Fix discrepancies before declaring completion.

---

# 33. FINAL DELIVERABLE

Give me a complete Django project that I can download/open in VS Code and run locally.

The final project must contain:

- Complete Django backend
- Complete frontend
- All pages
- Database models
- Migrations
- Admin panel
- Demo data
- Contact system
- Google Form integration
- Responsive design
- Animations
- SEO
- Security configuration
- README
- requirements.txt
- .env.example

DO NOT give me only a prototype.

DO NOT give me only HTML.

DO NOT leave inner pages as placeholders.

DO NOT leave TODO comments for core functionality.

Build the complete working project.

FINAL PRIORITY:

1. Reference visual fidelity
2. Complete functionality
3. Responsive behavior
4. Animation/interactions
5. Clean Django architecture
6. Admin editability
7. Production readiness

Start by studying the reference preview carefully, then build the complete Django application.