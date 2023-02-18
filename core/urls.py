from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="IZZI API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('auth/', include('rest_framework.urls')),

    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


    path('api_auth/', include('users.urls')),
    path('api_services/', include('services.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Deployment
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
