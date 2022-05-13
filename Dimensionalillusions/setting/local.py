from Dimensionalillusions.base import *

from .environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

DEBUG = True

SITE_ID = 1

SECRET_KEY = env.str("SECRET_KEY")
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # Explict middleware
    "csp.middleware.CSPMiddleware",
]
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

"""
#Django Debugger Toolbar
#If you don't include this, It wont show
ensure django.contrib.staticfiles is in INSTALLED_APPS
"""

INTERNAL_IPS = [
    "127.0.0.1",
]

"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

"""

DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE"),
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.str("DATABASE_PORT"),
    }
}


# Content Security Policy
CSP_DEFAULT_SRC = ("none",)
CSP_BASE_URI = ("'none'",)
CSP_FRAME_ANCESTORS = ("'none'",)
CSP_OBJECT_SRC = ("none",)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    "cdn.jsdelivr.net",
    "cdnjs.cloudflare.com",
    "fonts.googleapis.com",
    "stackpath.bootstrapcdn.com",
    "getbootstrap.com",
)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "clipboardjs.com",
    "ajax.googleapis.com",
    "cdn.jsdelivr.net",
    "cdn.ckeditor.com",
    "stackpath.bootstrapcdn.com",
    "code.jquery.com",
    "unpkg.com",
    "cdnjs.cloudflare.com",
    "code.jquery.com",
    "getbootstrap.com",
)
CSP_IMG_SRC = ("'self'", "* data:", "cdn.jsdelivr.net", "res.cloudinary.com")
CSP_FONT_SRC = ("'self'", "cdnjs.cloudflare.com", "cdn.jsdelivr.net", "fonts.googleapis.com", "fonts.gstatic.com")

CSP_FRAME_SRC = ("'self'",)
CSP_CONNECT_SRC = (
    "'self'",
    "http://*.cke-cs.com",
    "https://docx-converter.cke-cs.com",
    "https://pdf-converter.cke-cs.com",
)


"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str("DATABASE_NAME"),  
        'USER': env.str("DATABASE_USER"),    
        'PASSWORD': env.str("DATABASE_PASSWORD"),  
        'HOST': env.str("DATABASE_HOST"),
        'PORT': env.str("DATABASE_PORT"),
    }
}

"""

import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES["default"].update(db_from_env)


STATIC_URL = "/staticfiles/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
"""
In production, all of your static files must exist in a directory
i.e. STATIC_ROOT and your web server should serve them to the public i.e. STATIC_URL.
"""
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_ROOT = os.path.join(BASE_DIR, "staticfiles/mediafiles")
MEDIA_URL = "/mediafiles/"

# DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


# SMTP CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = env.str("Email_Host_User")
EMAIL_HOST_PASSWORD = env.str("Email_Host_Password")
