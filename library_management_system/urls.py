from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.views import HomeView, BookDetailsView

urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path(
        "books/book/<int:id>/book_details",
        BookDetailsView.as_view(),
        name="book_details",
    ),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    # path("", include("core.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
