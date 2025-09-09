from django.contrib import admin
# The fix is on this line: we import the correct model name.
from .models import SupportTicket

# This line registers your model with the Django admin site.
admin.site.register(SupportTicket)