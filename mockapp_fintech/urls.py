# mockapp_fintech/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mockapp Fintech</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background: #f8f9fa;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
            }
            .header {
                background: #fff;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                padding: 1rem 0;
                margin-bottom: 2rem;
            }
            .header h1 {
                margin: 0;
                padding: 0 2rem;
                color: #2c3e50;
            }
            .card {
                background: white;
                border-radius: 8px;
                padding: 2rem;
                margin-bottom: 1rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .links {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1rem;
                margin-top: 2rem;
            }
            .link-card {
                background: #fff;
                padding: 1.5rem;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transition: transform 0.2s ease;
            }
            .link-card:hover {
                transform: translateY(-3px);
            }
            .link-card h3 {
                margin: 0 0 1rem 0;
                color: #2c3e50;
            }
            .link-card p {
                margin: 0;
                color: #666;
            }
            .button {
                display: inline-block;
                padding: 0.5rem 1rem;
                background: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 4px;
                margin-top: 1rem;
            }
            .button:hover {
                background: #2980b9;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Mockapp Fintech Platform</h1>
        </div>
        <div class="container">
            <div class="card">
                <h2>Welcome to Our Financial Management Platform</h2>
                <p>Access and manage your investments and insurance policies in one place.</p>
            </div>
            
            <div class="links">
                <div class="link-card">
                    <h3>💼 Admin Portal</h3>
                    <p>Manage users, investments, and insurance policies</p>
                    <a href="/admin/" class="button">Access Admin</a>
                </div>
                
                <div class="link-card">
                    <h3>🔌 API Endpoints</h3>
                    <p>Direct access to our REST API endpoints</p>
                    <a href="/api/" class="button">View API</a>
                </div>
                
                <div class="link-card">
                    <h3>📝 API Documentation</h3>
                    <p>Explore our API documentation</p>
                    <a href="/swagger/" class="button">View Docs</a>
                </div>
            </div>
        </div>
        
        <!-- AICSM Chat Widget -->
        <div id="VG_OVERLAY_CONTAINER" style="width: 0; height: 0;">
        </div>
        <script defer>
        (function() {
            window.VG_CONFIG = {
                ID: "u8me7urttv9ryhbo",
                region: 'na',
                render: 'bottom-right',
                stylesheets: [
                    "https://vg-bunny-cdn.b-cdn.net/vg_live_build/styles.css",
                ],
            }
            var VG_SCRIPT = document.createElement("script");
            VG_SCRIPT.src = "https://vg-bunny-cdn.b-cdn.net/vg_live_build/vg_bundle.js";
            VG_SCRIPT.defer = true;
            document.body.appendChild(VG_SCRIPT);
        })()
        </script>
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
]
