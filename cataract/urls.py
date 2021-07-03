from django.contrib import admin
from . import views

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cat, name='home')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)