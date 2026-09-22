from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/'.env')
SECRET_KEY=os.getenv('DJANGO_SECRET_KEY','change-me-in-production')
DEBUG=os.getenv('DEBUG','False').lower()=='true'
ALLOWED_HOSTS=[h.strip() for h in os.getenv('ALLOWED_HOSTS','127.0.0.1,localhost').split(',') if h.strip()]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','website']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='config.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='config.wsgi.application'
DATABASES={'default':dj_database_url.config(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}', conn_max_age=600)}
AUTH_PASSWORD_VALIDATORS=[]
LANGUAGE_CODE='en-us'; TIME_ZONE='Asia/Kolkata'; USE_I18N=True; USE_TZ=True
STATIC_URL='/static/'; STATIC_ROOT=BASE_DIR/'staticfiles'; STATICFILES_DIRS=[BASE_DIR/'website/static']
STORAGES={'default':{'BACKEND':'django.core.files.storage.FileSystemStorage'},'staticfiles':{'BACKEND':'whitenoise.storage.CompressedManifestStaticFilesStorage'}}
MEDIA_URL='/media/'; MEDIA_ROOT=BASE_DIR/'media'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
GOOGLE_FORM_URL=os.getenv('GOOGLE_FORM_URL','')
GOOGLE_FORM_ENTRY_NAME=os.getenv('GOOGLE_FORM_ENTRY_NAME','')
GOOGLE_FORM_ENTRY_EMAIL=os.getenv('GOOGLE_FORM_ENTRY_EMAIL','')
GOOGLE_FORM_ENTRY_PHONE=os.getenv('GOOGLE_FORM_ENTRY_PHONE','')
GOOGLE_FORM_ENTRY_PROJECT_TYPE=os.getenv('GOOGLE_FORM_ENTRY_PROJECT_TYPE','')
GOOGLE_FORM_ENTRY_BUDGET=os.getenv('GOOGLE_FORM_ENTRY_BUDGET','')
GOOGLE_FORM_ENTRY_MESSAGE=os.getenv('GOOGLE_FORM_ENTRY_MESSAGE','')
