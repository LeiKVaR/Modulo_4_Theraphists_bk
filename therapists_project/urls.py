from django.contrib import admin
from django.urls import path, include
from therapists.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),  #  esta línea muestra algo en /
    path('admin/', admin.site.urls),
    path('api/', include('therapists.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)