<<<<<<< HEAD
from doctest import FAIL_FAST

=======
>>>>>>> 61b8ce055a3439493fc86f88f4a4b2dfff461a95
from Dimensionalillusions.base import *

from .environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

<<<<<<< HEAD
DEBUG = False
SECRET_KEY = env.str("SECRET_KEY")
SITE_ID = 2

ALLOWED_HOSTS = [".up.railway.app", "dimensionalillusions.com", "www.dimensionalillusions.com"]
=======
DEBUG = True  # When DEBUG =True Caching will Take Place
SECRET_KEY = env.str("SECRET_KEY")
SITE_ID = 2

ALLOWED_HOSTS = ["acadepra.herokuapp.com", "acadepra.com", "www.acadepra.com"]
>>>>>>> 61b8ce055a3439493fc86f88f4a4b2dfff461a95
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",  # Explict middleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",  # Explict middleware
    "csp.middleware.CSPMiddleware",
]

SESSION_COOKIE_AGE = 60 * 60 * 60 * 24

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
<<<<<<< HEAD

"""
 specifies valid parents that may embed a page using <frame>, 
 <iframe>, <object>, <embed>, or <applet>.
"""
CSP_FRAME_ANCESTORS = ("'none'",)


=======
CSP_FRAME_ANCESTORS = ("'none'",)
>>>>>>> 61b8ce055a3439493fc86f88f4a4b2dfff461a95
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
<<<<<<< HEAD
    "connect.facebook.net",
=======
>>>>>>> 61b8ce055a3439493fc86f88f4a4b2dfff461a95
    "stackpath.bootstrapcdn.com",
    "code.jquery.com",
    "unpkg.com",
    "cdnjs.cloudflare.com",
    "code.jquery.com",
    "getbootstrap.com",
)
CSP_IMG_SRC = ("'self'", "* data:", "cdn.jsdelivr.net", "res.cloudinary.com")
CSP_FONT_SRC = ("'self'", "cdnjs.cloudflare.com", "cdn.jsdelivr.net", "fonts.googleapis.com", "fonts.gstatic.com")

<<<<<<< HEAD

"""
frame-src
The HTTP Content-Security-Policy (CSP) frame-src directive specifies valid sources for nested
 browsing contexts loading using elements such as <frame> and <iframe>.
"""
CSP_FRAME_SRC = (
    "'self'",
    "https://www.facebook.com",
)

"""
guards the several browsers mechanisms that can fetch HTTP Requests.
"""

CSP_CONNECT_SRC = (
    "'self'",
    "https://www.facebook.com",
    "https://fonts.googleapis.com",
=======
CSP_FRAME_SRC = ("'self'",)
CSP_CONNECT_SRC = (
    "'self'",
>>>>>>> 61b8ce055a3439493fc86f88f4a4b2dfff461a95
    "http://*.cke-cs.com",
    "https://docx-converter.cke-cs.com",
    "https://pdf-converter.cke-cs.com",
)


# CACHE FRAMEWORK
CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 60  # 1 week
CACHE_MIDDLEWARE_KEY_PREFIX = ""

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 15780000  # 6 Months as Recommended
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# CSRF
CSRF_COOKIE_SECURE = True  # to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True  # to avoid transmitting the session cookie over HTTP accidentally.

# REDIRECT HTTP TO HTTPS
SECURE_SSL_REDIRECT = True


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
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# SMTP CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = env.str("Email_Host_User")
EMAIL_HOST_PASSWORD = env.str("Email_Host_Password")
<<<<<<< HEAD


CSRF_TRUSTED_ORIGINS = [
    "https://dimensionalillusions.up.railway.app",
]
=======
>>>>>>> 61b8ce055a3439493fc86f88f4a4b2dfff461a95
