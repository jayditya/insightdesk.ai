from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    response = models.TextField(null=True, blank=True)  # ✅ Fix applied
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ticket from {self.name} - {self.email}'
