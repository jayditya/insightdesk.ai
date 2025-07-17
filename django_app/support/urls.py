from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_ticket, name='submit_ticket'),
    path('submitted/<int:ticket_id>/', views.ticket_submitted, name='ticket_submitted'),
    path('logout/', views.logout_view, name='logout'),
]
