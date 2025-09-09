from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This tells Django that any URL that is NOT 'admin/'
    # should be handled by the 'support.urls' file.
    path('', include('support.urls')),
]