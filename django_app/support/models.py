from django.db import models

# This class defines the structure of a support ticket in your database.
class SupportTicket(models.Model):
    # A field for the user's name, up to 100 characters.
    name = models.CharField(max_length=100)
    
    # A field for the user's email.
    email = models.EmailField()
    
    # A large text field for the user's support message.
    message = models.TextField()
    
    # A text field for the AI's response. It can be blank initially.
    response = models.TextField(blank=True, null=True)
    
    # A timestamp that is automatically set when a ticket is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # This is a helper method to display the ticket nicely in the admin area.
    def __str__(self):
        return f"Ticket from {self.name} on {self.created_at.strftime('%Y-%m-%d')}"

