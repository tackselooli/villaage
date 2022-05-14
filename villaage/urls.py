from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('supersecret/', admin.site.urls),
                  path('api/v1/auth/', include('djoser.urls')),
                  path('api/v1/auth/', include('djoser.urls.jwt')),
                  path('api/v1/profile/', include('apps.profiles.urls')),
                  path('api/v1/properties/', include('apps.properties.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Villaage Admin'
admin.site.site_title = 'Villaage Admin Portal'
admin.site.index_title = 'welcome to the Villaage portal'
