from rest_framework import serializers
from .models import Card, Invoice, User

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = "__all__"

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'card_no', 'cardholder_name', 'expiry_date', 'cvv', 'balance', 'user']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_no', 'name', 'status']