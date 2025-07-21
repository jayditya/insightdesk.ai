from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm
import requests

def submit_ticket(request):
    hide_user_fields = False
    user_name = request.session.get('user_name')
    user_email = request.session.get('user_email')

    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)

            # Save to session
            request.session['user_name'] = form.cleaned_data['name']
            request.session['user_email'] = form.cleaned_data['email']

            # Send to Flask for AI response
            response = requests.post('https://insightdesk-ml.onrender.com/predict', json={"message": ticket.message})
            if response.ok:
                ticket.response = response.json().get('response', 'AI could not generate a response.')
            else:
                ticket.response = 'AI service is unavailable.'

            ticket.save()
            return redirect('ticket_submitted', ticket_id=ticket.id)
    else:
        initial_data = {}
        if user_name and user_email:
            hide_user_fields = True
            initial_data['name'] = user_name
            initial_data['email'] = user_email

        form = TicketForm(initial=initial_data)

    return render(request, 'support/submit_ticket.html', {
        'form': form,
        'hide_user_fields': hide_user_fields,
        'user_name': user_name
    })

def ticket_submitted(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    user_name = request.session.get('user_name')
    return render(request, 'support/ticket_submitted.html', {
        'ticket': ticket,
        'user_name': user_name
    })

def logout_view(request):
    request.session.flush()
    return redirect('submit_ticket')
