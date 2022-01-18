from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls'), name="catalog"),
    path('accounts/', include('django.contrib.auth.urls')),
]
