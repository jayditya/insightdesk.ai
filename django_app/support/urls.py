from django.urls import path
from . import views

urlpatterns = [
    # The main page for submitting a ticket
    path('', views.submit_ticket_view, name='submit_ticket'),
    
    # The page for the dashboard (list of all tickets)
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # --- THIS IS OUR NEW URL ---
    # It handles URLs like /submitted/1/, /submitted/2/, etc.
    # and calls our new view function.
    path('submitted/<int:ticket_id>/', views.ticket_submitted_view, name='ticket_submitted'),
    # ---------------------------
    
    # The URL for logging out
    path('logout/', views.logout_view, name='logout'),
]