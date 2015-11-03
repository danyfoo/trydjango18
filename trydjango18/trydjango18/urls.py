from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact$', 'newsletter.views.contact', name='contact'),
    url(r'^about$', 'trydjango18.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
