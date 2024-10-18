from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import profile_view
from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('@<username>/', profile_view, name="profile"),
    # path('socialaccounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
    path('chat/', include('a_rtchat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
