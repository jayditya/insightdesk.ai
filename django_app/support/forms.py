from django import forms
# The fix is on this line: we import the correct model name.
from .models import SupportTicket

class TicketForm(forms.ModelForm):
    class Meta:
        # And we use the correct model name here as well.
        model = SupportTicket
        fields = ['name', 'email', 'message']