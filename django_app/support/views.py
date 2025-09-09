from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TicketForm
from .models import SupportTicket
import requests

# This view handles the main submission form
def submit_ticket_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            
            ai_response_text = "Sorry, the AI service is unavailable."
            try:
                # Django calls the Flask API
                api_url = 'http://127.0.0.1:5000/predict'
                response = requests.post(api_url, json={'message': user_message})
                if response.status_code == 200:
                    ai_response_text = response.json().get('response', 'Error parsing AI response.')
            except requests.exceptions.RequestException as e:
                print(f"ERROR: Could not connect to Flask API: {e}")
            
            # Save the ticket with the AI response
            ticket = form.save(commit=False)
            ticket.response = ai_response_text
            ticket.save()
            
            # Store user details in the session
            request.session['user_name'] = ticket.name
            
            # --- THIS IS THE KEY CHANGE ---
            # Instead of redirecting to the dashboard, we now redirect
            # to our new "ticket_submitted" page, passing the ID of the
            # ticket we just created.
            return redirect('ticket_submitted', ticket_id=ticket.id)
            # --------------------------------

    else:
        form = TicketForm()

    return render(request, 'support/submit_ticket.html', {
        'form': form,
        'user_name': request.session.get('user_name')
    })


# --- THIS IS OUR NEW VIEW FUNCTION ---
# It takes a ticket_id, finds that specific ticket in the database,
# and shows it on our new HTML page.
def ticket_submitted_view(request, ticket_id):
    ticket = get_object_or_404(SupportTicket, pk=ticket_id)
    return render(request, 'support/ticket_submitted.html', {
        'ticket': ticket,
        'user_name': request.session.get('user_name')
    })
# ------------------------------------


# This view for the dashboard remains the same
def dashboard_view(request):
    tickets = SupportTicket.objects.all().order_by('-created_at')
    return render(request, 'support/dashboard.html', {
        'tickets': tickets,
        'user_name': request.session.get('user_name')
    })

# This view for logout remains the same
def logout_view(request):
    request.session.flush()
    messages.info(request, "You have been logged out.")
    return redirect('submit_ticket')