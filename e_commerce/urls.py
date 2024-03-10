from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from e_commerce import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Users.urls")),
    path("", include("shop.urls")),
    path("", include("cart.urls")),
    path("", include("order.urls")),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("cookie-policy/", views.cookie_policy, name="cookie_policy"),
    path("terms-conditions/", views.terms_conditions, name="terms_conditions"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
