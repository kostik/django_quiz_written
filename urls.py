from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from .views import login_form_page

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^exam/', include('quiz.urls')),
                       url(r'^$', login_form_page, name='home'),
                       url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^i18n/', include('django.conf.urls.i18n')),

                       url('^accounts/', include('django.contrib.auth.urls')),
                       url('^accounts/', include('registration.backends.default.urls')),
                       url(r'^accounts/logout$', 'django.contrib.auth.views.logout',
                           {'next_page': reverse_lazy("home")}
                           ),

                       url('^written/', include('generator.urls'))

                       )

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
