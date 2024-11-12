# mockapp_fintech/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simplest possible home view
def home(request):
    return HttpResponse("Mockapp Fintech is running. Access /admin for administration or /api for API endpoints.")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
