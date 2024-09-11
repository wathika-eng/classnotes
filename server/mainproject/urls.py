from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.auth.models import User
from django.views.static import serve
from django.conf.urls.static import static

# from django_otp.admin import OTPAdminSite
# from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


# class OTPAdmin(OTPAdminSite):
#     pass


# admin_site = OTPAdmin(name="OTPAdmin")
# admin_site.register(User)
# admin_site.register(TOTPDevice, TOTPDeviceAdmin)

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"api/", include("mainapp.urls")),
    path(r"api-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # path('auth/', include('social_django.urls', namespace='social')),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    # url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "mainapp.views.error_404_view"  # if debug = False
