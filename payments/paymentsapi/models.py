from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

class Card(models.Model):
    card_no = CardNumberField()
    cardholder_name = models.CharField(max_length=50)
    expiry_date = CardExpiryField()
    cvv = SecurityCodeField()
    balance = models.FloatField()
    
    def __str__(self):
        return self.card_no

