from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request: redirect('support/', permanent=False)),
    path('admin/', admin.site.urls),
    path('support/', include('support.urls')),
    path('dashboard/', include('dashboard.urls')),
]
