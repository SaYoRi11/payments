from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    balance = models.FloatField(default = 0)
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username)

class Card(models.Model):
    card_no = CardNumberField()
    cardholder_name = models.CharField(max_length=50)
    expiry_date = CardExpiryField()
    cvv = SecurityCodeField()
    balance = models.FloatField()
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_details', null=True)
    
    def __str__(self):
        return self.card_no

class Invoice(models.Model):
    status_choices = (
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Approved')
    )

    amount = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    def __str__(self):
        return str(self.id)


