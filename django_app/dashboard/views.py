from django.shortcuts import render
from support.models import Ticket  # Import the Ticket model

def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')  # Most recent first
    return render(request, 'dashboard/ticket_list.html', {'tickets': tickets})
