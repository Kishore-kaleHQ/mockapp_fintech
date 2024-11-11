from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from hello.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),  # Root URL points to the hello_world view
]
