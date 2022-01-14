from django.contrib import admin
from django.urls import include, path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.conf import settings
from django.conf.urls.static import static
from pages.views import search, ContactFormView
from users.views import AuthorListView

# /kontakt
# /admin
# /polls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('api/polls/', include('polls.api_urls')),
    # wagtail urls
    path('admin/', include(wagtailadmin_urls)),
    path('accounts/', include('allauth.urls')),
    # path('documents/', include(wagtaildocs_urls)),
    # default na konci
    path('search/', search, name='search'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('', include(wagtail_urls)),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)