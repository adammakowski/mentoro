from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

def trigger_error(request):
    division_by_zero = 1 / 0

# if bool(settings.DEBUG):
#     import debug_toolbar

urlpatterns = [
    # sentry werify
    path('sentry-debug/', trigger_error),
    # Django Debug Toolbar https://github.com/jazzband/django-debug-toolbar
    # path('__debug__/', include(debug_toolbar.urls)),
    # admin path
    path('admin/', admin.site.urls),
    # sites path
    path('', include('home.urls')),
    # accounts app paths
    path('accounts/', include('accounts.urls')),
    # dashboard path
    path('dashboard/', include('dashboard.urls')),
    # Mentoro|Courses path
    path('courses/', include('courses.urls')),
    # Mentoro|Library path
    path('library/', include('library.urls')),
    # users auth
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
