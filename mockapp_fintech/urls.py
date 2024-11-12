# mockapp_fintech/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

def home(request):
    html_content = """
    <html>
        <head>
            <title>Mockapp Fintech</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
                .container { max-width: 800px; margin: 0 auto; }
                .links a { display: inline-block; margin: 10px; }
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

schema_view = get_schema_view(
    openapi.Info(
        title="Mockapp Fintech API",
        default_version='v1',
        description="API documentation for Mockapp Fintech platform",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Home page
    path('', home, name='home'),
    
    # Existing paths
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
