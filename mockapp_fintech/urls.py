# mockapp_fintech/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mockapp Fintech API",
        default_version='v1',
        description="API documentation for fintech platform",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(),
)

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mockapp Fintech</title>
        <style>
            body { font-family: system-ui, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; }
            .links a { display: inline-block; margin: 10px; padding: 10px 20px; 
                      background: #007bff; color: white; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Mockapp Fintech</h1>
            <div class="links">
                <a href="/admin/">Admin Interface</a>
                <a href="/api/">API Endpoints</a>
                <a href="/swagger/">API Documentation</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
