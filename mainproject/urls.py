from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path(r'admin', admin.site.urls),
    path(r'', include("mainapp.urls")),
    path(r'', include('django.contrib.auth.urls')),
    # path('auth/', include('social_django.urls', namespace='social')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'mainapp.views.error_404_view' #if debug = False
