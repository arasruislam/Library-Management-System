from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("admin/", admin.site.urls),
    # path("account/", include("accounts.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
