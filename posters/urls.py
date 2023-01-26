from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls', namespace='home')),
    path('account/', include('account.urls', namespace='account')),
    path('posters/', include('poster.urls', namespace='poster')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)