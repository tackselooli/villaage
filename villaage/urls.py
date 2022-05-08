from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
                  path('supersecret/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Villaage Admin'
admin.site.site_title = 'Villaage Admin Portal'
admin.site.index_title = 'welcome to the Villaage portal'
