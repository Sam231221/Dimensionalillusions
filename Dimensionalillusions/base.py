import os
import site
from pathlib import Path

from django.utils import tree

BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.staticfiles",
]

EXPLICT_APPS = [
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "Dimensionalillusions.apps.EHub",
    "Dimensionalillusions.apps.MCourses",
    "Dimensionalillusions.apps.MArticles",
    "Dimensionalillusions.apps.MProgrammingLanguage",
    "Dimensionalillusions.apps.MSoftwareDevelopment",
]

THIRDPARTY_PLUGIN = [
    "ckeditor",
    "ckeditor_uploader",
    "taggit",
    "mptt",
    "debug_toolbar",
    "whitenoise",
]

# only if django version >= 3.0
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]


INSTALLED_APPS = DEFAULT_APPS + EXPLICT_APPS + THIRDPARTY_PLUGIN
APP_DIRS = True


CKEDITOR_UPLOAD_PATH = "ckeditor/uploads/"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "uiColor": "#FFFFFF",
        "height": 500,
        "toolbar_Custom": [
            ["Styles", "Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker", "Undo", "Redo"],
            ["Link", "Unlink", "Anchor"],
            ["Image", "Flash", "Table", "HorizontalRule"],
            ["TextColor", "BGColor"],
            ["Smiley", "SpecialChar"],
            ["Source"],
        ],
    },
    "sourcecode": {
        "skin": "moono",
        # 'skin': 'office2013',
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {"name": "document", "items": ["Source", "-", "Save", "NewPage", "Preview", "Print", "-", "Templates"]},
            {
                "name": "clipboard",
                "items": ["Cut", "Copy", "Paste", "PasteText", "PasteFromWord", "-", "Undo", "Redo"],
            },
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            {
                "name": "insert",
                "items": ["Image", "Flash", "Table", "HorizontalRule", "Smiley", "SpecialChar", "PageBreak", "Iframe"],
            },
            "/",
            {
                "name": "basicstyles",
                "items": ["Bold", "Italic", "Underline", "Strike", "Subscript", "Superscript", "-", "RemoveFormat"],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "CreateDiv",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "BidiLtr",
                    "BidiRtl",
                    "Language",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            "\t",
            {
                "name": "tools",
                "items": [
                    "CodeSnippet",
                    "youtube",
                    "clipboard",
                    "ShowBlocks",
                    "Preview",
                    "Maximize",
                ],
            },
            "/",  # put this to force next toolbar on new line
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        "toolbarGroups": [{"name": "document", "groups": ["mode", "document", "doctools"]}],
        "width": "100%",
        "removePlugins": "stylesheetparser",
        "toolbarCanCollapse": True,
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                "codesnippet",
                "widget",
                "lineutils",
                "clipboard",
                "elementspath",
            ]
        ),
    },
}


'''
We are telling heroku to use gunicorn web server through Procfile created in same directory as manage.py"""
'''

ROOT_URLCONF = "Dimensionalillusions.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "Dimensionalillusions.apps.EHub.context_processors.forms",
                "Dimensionalillusions.apps.MProgrammingLanguage.context_processors.programminglanguages",
                "Dimensionalillusions.apps.MSoftwareDevelopment.context_processors.frameworks",
                "Dimensionalillusions.apps.MArticles.context_processors.articlefilters",
            ],
        },
    },
]

WSGI_APPLICATION = "Dimensionalillusions.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SESSION_COOKIE_AGE = 24 * 60 * 60


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Dimensionalillusions Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Dimensionalillusions",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Dimensionalillusions",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "assets/img/favicon.png",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Text on the admin login page screen
    "welcome_sign": "Dimensionalillusions Adminsitration",
    # Copyright on the footer
    "copyright": "Dimensional illusions pvt ltd",
    # The model admin to search from the search bar, search bar omitted if excluded
    # "search_model": "auth.User",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    # "user_avatar": None,
    # Top Menu Navbar #
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "books"},
    ],
    # User Menu located top right #("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Youtube", "url": "https://www.youtube.com/", "new_window": True},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"},
    ],
    # Use modals instead of popups
    "related_modal_active": True,
}


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kathmandu"
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
