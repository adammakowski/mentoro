from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import debug_toolbar

# Sentry SDK
def trigger_error(request):
    division_by_zero = 1 / 0


# Django Debug Toolbar
if bool(settings.DEBUG):
    import debug_toolbar


urlpatterns = [
    # sentry werify
    path('sentry-debug/', trigger_error),  # Sentry SDK
    path('__debug__/', include(debug_toolbar.urls)),  # Django Debug Toolbar https://github.com/jazzband/django-debug-toolbar
    # admin path
    path('admin/', admin.site.urls),
    # defender admin
    path('admin/defender/', include('defender.urls')),
    # Ckeditor uploader
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # sites path
    path('', include('home.urls')),
    # accounts app paths
    path('account/', include('accounts.urls')),
    # dashboard path
    path('dashboard/', include('dashboard.urls')),
    # Mentoro|Courses path
    path('courses/', include('courses.urls')),
    # Mentoro|Mentors path
    path('mentors/', include('mentors.urls')),
    # Mentoro|Library path
    path('library/', include('library.urls')),
    # Mentoro|Blog path
    path('blog/', include('blog.urls')),
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
