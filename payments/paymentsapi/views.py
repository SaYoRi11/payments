from rest_framework import viewsets, views, status
from .models import Card, Invoice, User
from .serializers import CardSerializer, InvoiceSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class PayByCardView(views.APIView):
    def post(self, request):
        invoice_id = request.data.get('invoice_id')
        name = request.data.get('cardholder_name')
        card_no = request.data.get('card_no')
        expiry_date = request.data.get('expiry_date')
        cvv = request.data.get('cvv')

        invoice = get_object_or_404(Invoice, pk=invoice_id)
        card = Card.objects.filter(card_no=card_no, cardholder_name=name, expiry_date=expiry_date, cvv=cvv)
        
        if not card:
            return Response('Card not found!', status=status.HTTP_400_BAD_REQUEST)
        else:
            if card[0].balance < invoice.amount:
                invoice.status = "Rejected"
                invoice.save()
                return Response('Insufficient balance', status=status.HTTP_400_BAD_REQUEST)
            else:
                card[0].balance = card[0].balance - invoice.amount
                invoice.status = "Approved"
                card[0].save()
                invoice.save()
                return Response(f"Paid successfully! Remaining balance: {card[0].balance}", status = status.HTTP_200_OK)

class PayByGOFAAView(views.APIView):
    def post(self, request):
        invoice_id = request.data.get('invoice_id')
        user_id = request.data.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        invoice = get_object_or_404(Invoice, pk=invoice_id)

        if user.balance < invoice.amount:
            invoice.status="Rejected"
            invoice.save()
            return Response("Insufficient balance", status=status.HTTP_400_BAD_REQUEST)

        user.balance = user.balance - invoice.amount
        invoice.status = "Approved"
        user.save()
        invoice.save()
        return Response(f"Paid Successfully! Remaining balance: {user.balance}", status = status.HTTP_200_OK)