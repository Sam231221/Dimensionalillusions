import debug_toolbar
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

"""
url() uses a regular expression to pattern match the
URL in your browser to a module in your Django project.
"""
urlpatterns = [  # contains list of url() instances.
    url(r"^admin/", admin.site.urls),
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),
    url(r"^", include("Dimensionalillusions.apps.EHub.urls", namespace="Ehub")),
    url(r"^", include("Dimensionalillusions.apps.MArticles.urls", namespace="MArticles")),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns


# page_not_found() view is overridden by handler404:
# The server_error() view is overridden by handler500:
# visit https://docs.djangoproject.com/en/dev/topics/http/views/#customizing-error-views

handler404 = "Dimensionalillusions.apps.EHub.views.response404_error_handler"
handler500 = "Dimensionalillusions.apps.EHub.views.response500_error_handler"

"""
Note: We are just providin the info of where is the custom page to be displayed
for the handler404 and handler500.
It can be created in any  one app.
"""

